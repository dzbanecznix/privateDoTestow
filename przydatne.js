async function getCode(url){
const browser = await puppeteer.launch();
const page = await browser.newPage();
await page.goto('https://raw.githubusercontent.com/dzbanecznix/privateDoTestow/master/h');
const pg = await page.content();
srccode = pg.substr(84, pg.length-104);
await browser.close();
var parser = new DOMParser().parseFromString(srccode, "text/html");
return parser.documentElement.textContent;}
