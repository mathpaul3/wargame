# Main Concept

- Web Scraping

## Explanation

If you are using Chrome,

**Step 1**: Check the token on the screen  
**Step 2**: Check the token in `Developer Tools > Elements`  
**Step 3**: Check the token in `Developer Tools > Console`  
**Step 4**: Check the token in `Developer Tools > Sources > styles.css`  
**Step 5**: Check the token in `Developer Tools > Sources > thingy.css`  
**Step 6**: Check the token in `Developer Tools > Network > 'suggestion' request > Headers > Response Headers > X-Token`  
**Step 7**: Check the token in `Developer Tools > Application > Cookies > a-token`  
**Step 8**: Check disallowed URLs from `${HOST}/robots.txt`  
Check the token in `${HOST}/a-magical-token.txt`  
**Step 9**: Check the token in `${HOST}/sitemap.xml`  
**Step 10**: Check the token by making a DELETE request to `${HOST}/` using an HTTP client (e.g., Python, Postman, Insomnia...)  
**Step 11**: Check the token by retrieving the TXT record of `i-spy.chall.lac.tf` using a DNS client (e.g., Python, nslookup, host...)

Or, you can perform all these steps using Python.
