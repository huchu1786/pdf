const puppeteer = require('puppeteer');

(async () => {
    try {
        const browser = await puppeteer.launch();
        const page = await browser.newPage();
        
        let errors = [];
        page.on('console', msg => {
            if (msg.type() === 'error') {
                errors.push(`Console Error: ${msg.text()}`);
            }
        });
        page.on('pageerror', error => {
            errors.push(`Page Error: ${error.message}`);
        });
        page.on('response', response => {
            if (!response.ok()) {
                errors.push(`Network Error: ${response.status()} ${response.url()}`);
            }
        });

        await page.goto('http://127.0.0.1:8080', { waitUntil: 'networkidle0' });
        
        if (errors.length > 0) {
            console.log('Errors found:');
            errors.forEach(e => console.log(e));
        } else {
            console.log('No errors found during page load.');
        }
        
        // Take a screenshot instead of video
        await page.screenshot({ path: 'output.png', fullPage: true });
        console.log('Screenshot saved to output.png');
        
        await browser.close();
    } catch (e) {
        console.error('Puppeteer Script Error:', e);
    }
})();
