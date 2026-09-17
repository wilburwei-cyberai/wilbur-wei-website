// Regression checks for the v3 content, lab identity and compact status labels.
const {chromium}=require(process.env.WILBUR_PLAYWRIGHT_MODULE || 'playwright');
const assert=require('assert');
const fs=require('fs');
const path=require('path');
(async()=>{
 const browser=await chromium.launch({headless:true,channel:process.env.WILBUR_BROWSER_CHANNEL || 'chrome'});
 const base=process.env.WILBUR_PREVIEW_URL || 'http://127.0.0.1:8768';
 const output=process.env.WILBUR_QA_DIR || path.resolve(__dirname,'../../網站v3檢查');
 fs.mkdirSync(output,{recursive:true});
 let badges=0;
 const errors=[];
 try {
  for(const width of [1440,390]) {
   const page=await browser.newPage({viewport:{width,height:960}});
   page.on('pageerror',e=>errors.push(e.message));
   for(const lang of ['', 'en/']) {
    await page.goto(`${base}/${lang}experience/`,{waitUntil:'networkidle'});
    assert.equal(await page.locator('#A11 .record-year').textContent(),'2025');
    await page.locator('#record-search').fill('SEMICON');
    assert.equal(await page.locator('[data-record]:visible').count(),1);
    assert(await page.locator('#A11').isVisible());
    await page.locator('#record-search').fill('');
    assert.equal(await page.locator('#A8 .record-year').textContent(),'2026');
    assert.equal(await page.locator('#A8 .meta').textContent(),lang?'Kamee Inc. · Internal corporate talk':'咖米股份有限公司 · 企業內部演講');
    for(const tag of await page.locator('[data-record] .tag').all()){
      const box=await tag.boundingBox();
      assert(box.height<=36 && box.width<=180,`oversized status ${await tag.textContent()} at ${width}`);
      assert.notEqual(await tag.evaluate(el=>getComputedStyle(el).display),'grid');
      badges++;
    }
    if(!lang) for(const id of ['A8','B13']) {
      await page.locator('#'+id).screenshot({path:path.join(output,`record-${id}-${width}.png`)});
    }
    await page.goto(`${base}/${lang}consulting/`);
    const links=page.locator('#evidence .evidence-links a');
    assert.equal(await links.count(),2);
    assert.equal(await links.nth(0).getAttribute('href'),'https://yznews.yzu.edu.tw/index.php/zh/yzu-campus-news-zh/1042-3');
    assert.equal(await links.nth(1).getAttribute('href'),'https://www.cse.yzu.edu.tw/news/announcement?id=193');
    await page.goto(`${base}/${lang}`);
    assert.equal(await page.locator('#cases a[href="https://www.cse.yzu.edu.tw/news/announcement?id=193"]').count(),1);
    assert.equal(await page.locator('.profile-role').count(),3);
    assert.equal(await page.locator('.achievement-number').count(),4);
    assert((await page.locator('#achievements').textContent()).includes('2022 R&D 100 Awards'));
    assert(!(await page.locator('main').textContent()).includes('91%'));
    assert.equal(await page.locator('#portfolio article.card').count(),4);
    assert.equal(await page.locator('#portfolio img').count(),0);
    const person=JSON.parse(await page.locator('script[type="application/ld+json"]').textContent())['@graph'].find(n=>n['@type']==='Person');
    assert.equal(person.sameAs[0],'https://www.cse.yzu.edu.tw/people/professor?name=Wilbur%20Wei');
    const teaser=page.locator('#mirage-lab img');
    await teaser.scrollIntoViewIfNeeded();await teaser.evaluate(img=>img.decode());
    assert(await teaser.evaluate(img=>img.naturalWidth===692));
    await page.goto(`${base}/${lang}lab/`);
    const graph=JSON.parse(await page.locator('script[type="application/ld+json"]').textContent())['@graph'];
    assert(graph.some(n=>n['@type']==='Organization' && n.name==='MIRAGE Lab'));
    assert.equal(await page.locator('.lab-hero img').getAttribute('alt'),'MIRAGE Lab — 代理人紅隊攻防實境實驗室');
    assert.equal(await page.locator('.lab-advisor img').count(),1);
   }
   await page.close();
  }
  assert.equal(badges,92);
  assert.equal(errors.length,0,errors.join('\n'));
  fs.writeFileSync(path.join(output,'v3-results.json'),JSON.stringify({compactStatusLabels:badges,checks:['Kamee 2026 internal corporate talk','two correctly attributed consulting links','homepage Zyell announcement','MIRAGE logo on homepage and lab page','lab entity in both languages','restored hero and three-role profile','achievement figures and R&D 100','SEMICON 2025 text-only record consistent with other talks','official faculty identity link'],errors},null,2));
  console.log('PASS: 92 compact status labels; Kamee date; collaboration links; MIRAGE branding; restored profile/achievements; SEMICON 2025; faculty identity.');
 } finally {await browser.close();}
})().catch(e=>{console.error(e);process.exit(1)});
