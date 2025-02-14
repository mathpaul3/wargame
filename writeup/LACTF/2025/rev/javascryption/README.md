# Main Concept

- Text Encoding

## Explanation

By visiting the given website and inspecting the HTML file, you can see `<script src="cabin.js"></script>` includes a reference to cabin.js, which contains the flag verification logic.

From `cabin.js`, you can find the `checkFlag` function, which processes the input flag through a series of transformations before comparing it to a predefined string.

- **step1**: Base64 encoding
- **step2**: Reversing the string
- **step3**: Replacing 'Z' with '[OLD_DATA]'
- **step4**: URI encoding
- **step5**: Base64 encoding

You can reverse the process to recover the original flag.
