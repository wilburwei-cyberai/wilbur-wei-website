// Focused regression for in-page inquiries. No email is sent or external draft opened.
const {chromium} = require(process.env.WILBUR_PLAYWRIGHT_MODULE || 'playwright');
const assert = require('assert');
const fs = require('fs');
const path = require('path');

(async () => {
  const browser = await chromium.launch({headless:true, channel:process.env.WILBUR_BROWSER_CHANNEL || 'chrome'});
  const base = process.env.WILBUR_PREVIEW_URL || 'http://127.0.0.1:8768';
  const output = process.env.WILBUR_QA_DIR || path.resolve(__dirname, '../../網站v3檢查');
  fs.mkdirSync(output, {recursive:true});
  const errors = [];
  let clicks = 0;
  try {
    for (const width of [1440,390]) {
      const page = await browser.newPage({viewport:{width,height:960}});
      page.on('pageerror', e => errors.push(e.message));
      // Exercise success and denial paths without overwriting the user's clipboard.
      await page.addInitScript(() => {
        Object.defineProperty(navigator, 'clipboard', {configurable:true, value:{writeText:async text => {
          if (window.denyCopy) throw new Error('Permission denied');
          window.copiedText = text;
        }}});
      });
      for (const lang of ['', 'en/']) {
        await page.goto(`${base}/${lang}`, {waitUntil:'networkidle'});
        const triggers = page.locator('#contact [data-inquiry]');
        assert.equal(await triggers.count(), 3);
        for (let i=0;i<3;i++) {
          const link = triggers.nth(i);
          const source = new URL(await link.getAttribute('href'));
          await link.click();
          const dialog = page.getByRole('dialog');
          assert(await dialog.isVisible(), `inquiry ${i} did not open at ${width} / ${lang}`);
          assert.equal(await page.locator('#inquiry-title').textContent(), source.searchParams.get('subject'));
          assert.equal(await page.locator('#inquiry-body').inputValue(), source.searchParams.get('body'));
          const box = await dialog.boundingBox();
          assert(box.x>=0 && box.x+box.width<=width+1);
          assert(!await dialog.evaluate(el => el.scrollWidth>el.clientWidth+1));
          const body = 'Test only / 測試\nA&B + ? # = café';
          await page.locator('#inquiry-body').fill(body);
          const subject = `QA ${i} & 測試`;
          await page.locator('#inquiry-subject').fill(subject);
          const mail = new URL(await page.locator('#inquiry-mail').getAttribute('href'));
          const gmail = new URL(await page.locator('#inquiry-gmail').getAttribute('href'));
          assert.equal(mail.protocol, 'mailto:');
          assert.equal(mail.pathname, 'wilbur.wei.cyberai@gmail.com');
          assert.equal(mail.searchParams.get('body'), body);
          assert.equal(mail.searchParams.get('subject'), subject);
          assert.equal(gmail.origin, 'https://mail.google.com');
          assert.equal(gmail.searchParams.get('to'), mail.pathname);
          assert.equal(gmail.searchParams.get('su'), subject);
          assert.equal(gmail.searchParams.get('body'), body);
          await page.locator('#inquiry-copy').click();
          const copied = await page.evaluate(() => window.copiedText);
          assert(copied.includes(body) && copied.includes(subject) && copied.includes(mail.pathname));
          assert((await page.locator('#inquiry-status').textContent()).length>0);
          await page.locator('#inquiry-copy-email').click();
          assert.equal(await page.evaluate(() => window.copiedText), mail.pathname);
          await page.keyboard.press('Escape');
          await page.waitForFunction(() => !document.documentElement.classList.contains('inquiry-open'));
          assert(!await dialog.isVisible());
          assert(await link.evaluate(el => el===document.activeElement));
          assert(!await page.evaluate(() => document.documentElement.classList.contains('inquiry-open')));
          // Closing and reopening the same inquiry preserves edits within this page.
          await link.click();
          assert.equal(await page.locator('#inquiry-body').inputValue(), body);
          await page.locator('.inquiry-close').click();
          await page.waitForFunction(() => !document.documentElement.classList.contains('inquiry-open'));
          clicks++;
        }
        await triggers.first().click();
        await page.evaluate(() => {window.denyCopy=true;});
        await page.locator('#inquiry-copy').click();
        assert(await page.locator('#inquiry-manual').isVisible());
        const manual = page.locator('#inquiry-copy-text');
        assert((await manual.inputValue()).includes('QA 0 & 測試'));
        assert(await manual.evaluate(el => el.selectionEnd===el.value.length && el.selectionStart===0));
        await page.locator('.inquiry-close').click();
        await page.waitForFunction(() => !document.documentElement.classList.contains('inquiry-open'));
        await page.evaluate(() => {window.denyCopy=false;});
      }
      await page.goto(base+'/');
      await page.locator('#contact [data-inquiry]').first().click();
      await page.screenshot({path:path.join(output,`inquiry-${width}.png`)});
      await page.close();
    }
    const page = await browser.newPage();
    await page.goto(base+'/consulting/');
    await page.locator('main [data-inquiry]').first().click();
    assert(await page.getByRole('dialog').isVisible());
    for(const lang of ['', 'en/']) {
      await page.goto(`${base}/${lang}lab/`);
      await page.locator('#lab-collaboration [data-inquiry]').click();
      assert(await page.getByRole('dialog').isVisible());
      assert.equal(await page.locator('#inquiry-email').inputValue(),'wilbur.wei@saturn.yzu.edu.tw');
      const academic = new URL(await page.locator('#inquiry-gmail').getAttribute('href'));
      assert.equal(academic.searchParams.get('to'),'wilbur.wei@saturn.yzu.edu.tw');
      assert(academic.searchParams.get('su').includes('MIRAGE Lab'));
    }
    const noJS = await browser.newContext({javaScriptEnabled:false});
    const plain = await noJS.newPage();
    await plain.goto(base+'/');
    assert(!await plain.locator('#inquiry-dialog').isVisible());
    assert.equal(await plain.locator('#contact [data-inquiry][href^="mailto:"]').count(),3);
    assert.equal(errors.length,0,errors.join('\n'));
    fs.writeFileSync(path.join(output,'inquiry-results.json'),JSON.stringify({inquiryChecks:clicks,errors,checks:['three actual clicks in both languages and viewports','draft editing and URL encoding','clipboard success/denial UI with test adapter','Escape and close restore focus','draft persistence within page','service-page inquiry','no-JS mailto fallback'],externalEmailActions:'not opened or sent'},null,2));
    console.log('PASS:',clicks,'inquiry flows; edit/copy/fallback/focus and no-JS checks. No email sent.');
  } finally {
    await browser.close();
  }
})().catch(error => {console.error(error);process.exit(1);});
