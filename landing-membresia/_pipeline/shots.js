// Uso: node shots.js <html> <outprefix>  → <outprefix>-desktop.png y <outprefix>-mobile.png (página completa)
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async () => {
  const [,, html, out] = process.argv;
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  for (const [n, w, h, m] of [['desktop',1280,800,false],['mobile',390,844,true]]) {
    const c = await b.newContext({ viewport:{width:w,height:h}, deviceScaleFactor: m?2:1, isMobile:m });
    const p = await c.newPage();
    await p.goto('file://' + require('path').resolve(html));
    await p.waitForTimeout(600);
    const sw = await p.evaluate(() => document.documentElement.scrollWidth);
    console.log(n, 'scrollWidth', sw, 'viewport', w, sw>w?'<<< OVERFLOW HORIZONTAL':'ok');
    await p.screenshot({ path: `${out}-${n}.png`, fullPage:true });
    await c.close();
  }
  await b.close();
})();
