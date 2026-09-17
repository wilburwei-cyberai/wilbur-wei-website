// Optional browser QA: npm install --no-save playwright, then node scripts/verify-browser.cjs
const {chromium}=require(process.env.WILBUR_PLAYWRIGHT_MODULE || 'playwright');
const fs=require('fs');
const path=require('path');
const assert=require('assert');
(async()=>{
 const browser=await chromium.launch({headless:true,channel:process.env.WILBUR_BROWSER_CHANNEL || 'chrome'});
 const errors=[];
 const base=process.env.WILBUR_PREVIEW_URL || 'http://127.0.0.1:8766';
 const output=process.env.WILBUR_QA_DIR || path.resolve(__dirname,'../../網站v1檢查');
 fs.mkdirSync(output,{recursive:true});
 const pages=['','speaking/','training/','consulting/','experience/','research/','about/','teaching/'];
 let checks=0;
 for(const width of [1440,390]) {
  const page=await browser.newPage({viewport:{width,height:960}});
  page.on('pageerror',e=>errors.push(e.message));
  for(const lang of ['', 'en/']) for(const slug of pages){
   await page.goto(`${base}/${lang}${slug}`,{waitUntil:'networkidle'});
   assert.equal(await page.locator('h1').count(),1);
   const overflow=await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth+1);
   assert(!overflow,`overflow ${width} ${lang}${slug}`);
   checks++;
  }
  await page.goto(base+'/',{waitUntil:'networkidle'});
  await page.screenshot({path:path.join(output,`home-${width}.png`),fullPage:true});
  await page.screenshot({path:path.join(output,`home-viewport-${width}.png`)});
  if(width===390){
    const toggle=page.getByRole('button',{name:'切換導覽選單'});
    await toggle.click(); assert.equal(await toggle.getAttribute('aria-expanded'),'true');
    await page.keyboard.press('Escape');assert.equal(await toggle.getAttribute('aria-expanded'),'false');
    await toggle.click();await page.locator('#site-nav a').filter({hasText:'企業內訓'}).click();
    assert(page.url().endsWith('/training/'));
  }
  await page.goto(base+'/research/',{waitUntil:'networkidle'});
  await page.screenshot({path:path.join(output,`research-${width}.png`),fullPage:true});
  await page.goto(base+'/en/',{waitUntil:'networkidle'});
  await page.screenshot({path:path.join(output,`home-en-${width}.png`),fullPage:true});
  await page.close();
 }
 // Check the desktop/mobile navigation boundary with the longer English labels.
 for(const width of [1024,768]) {
  const page=await browser.newPage({viewport:{width,height:960}});
  for(const lang of ['', 'en/']) {
   await page.goto(`${base}/${lang}`,{waitUntil:'networkidle'});
   assert(!await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth+1),`navigation overflow ${width} ${lang}`);
   if(width===1024){
    const brand=await page.locator('.brand').boundingBox();
    const nav=await page.locator('#site-nav').boundingBox();
    assert(brand.x+brand.width<nav.x,`navigation overlaps brand ${lang}`);
   } else {
    await page.locator('.nav-toggle').click();
    assert(await page.locator('#site-nav').isVisible());
   }
   checks++;
  }
  await page.close();
 }
 const page=await browser.newPage();
 await page.goto(base+'/experience/');
 await page.locator('#record-search').fill('咖米');
 assert.equal(await page.locator('[data-record]:visible').count(),1);
 await page.locator('#record-search').fill('');
 await page.selectOption('#record-kind','series');
 assert.equal(await page.locator('[data-record]:visible').count(),1);
 await page.selectOption('#record-kind','');
 await page.locator('#record-search').fill('zzzz-no-match');
 assert(await page.locator('#record-empty').isVisible());
 await page.goto(base+'/training/');
 await page.locator('#site-nav .language').click();assert(page.url().endsWith('/en/training/'));
 const mail=await page.locator('#contact a[href^="mailto:"]').first().getAttribute('href');
 const params=new URL(mail).searchParams;assert(params.get('subject'));assert(params.get('body').includes('How you found me'));
 const noJS=await browser.newContext({javaScriptEnabled:false,viewport:{width:390,height:844}});
 const plain=await noJS.newPage();await plain.goto(base+'/en/experience/');
 assert.equal(await plain.locator('[data-record]:visible').count(),22);
 assert(await plain.locator('#site-nav a').first().isVisible());
 assert.equal(await plain.locator('.nav-toggle:visible').count(),0);
 assert.equal(errors.length,0,errors.join('\n'));
 await browser.close();
 fs.writeFileSync(path.join(output,'browser-results.json'),JSON.stringify({pageViewportChecks:checks,consoleErrors:errors,checks:['mobile navigation / Escape','language counterpart','record search/type/empty state','email subject/body','no-JavaScript navigation and all 22 records']},null,2));
 console.log('PASS:',checks,'page/viewport checks; interaction, mailto and no-JavaScript checks. Screenshots:',output);
})().catch(e=>{console.error(e);process.exit(1)});
