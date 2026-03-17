#!/bin/bash

# 工具列表定义
declare -A tools=(
    # 文本计数类
    ["word-counter"]="Word Counter|Count words in your text instantly|word counting, word count tool"
    ["character-counter"]="Character Counter|Count characters and letters in your text|character count, letter counter"
    ["line-counter"]="Line Counter|Count the number of lines in your text|line count, count lines"
    ["sentence-counter"]="Sentence Counter|Count sentences in your text|sentence count, sentence counter"
    ["paragraph-counter"]="Paragraph Counter|Count paragraphs in your text|paragraph count, paragraph counter"
    
    # 文本生成/格式类
    ["lorem-ipsum-generator"]="Lorem Ipsum Generator|Generate Lorem Ipsum placeholder text|lorem ipsum, placeholder text generator"
    ["random-string-generator"]="Random String Generator|Generate random alphanumeric strings|random string, string generator"
    ["uuid-generator"]="UUID Generator|Generate unique UUIDs (v4)|uuid generator, unique id generator"
    ["password-generator"]="Password Generator|Generate strong secure passwords|password generator, strong password, random password"
    ["slug-generator"]="URL Slug Generator|Convert text to URL-friendly slugs|url slug, slug generator, url converter"
    
    # 文本转换类
    ["text-repeater"]="Text Repeater|Repeat text multiple times|text repeater, duplicate text"
    ["text-reverser"]="Reverse Text|Reverse your text backwards|reverse text, backwards text, text reverser"
    ["remove-duplicate-lines"]="Remove Duplicate Lines|Remove duplicate lines from text|remove duplicates, unique lines"
    ["remove-empty-lines"]="Remove Empty Lines|Remove all empty lines from text|remove blank lines, clean text"
    ["remove-line-breaks"]="Remove Line Breaks|Remove line breaks and newlines|remove line breaks, join lines"
    ["add-line-numbers"]="Add Line Numbers|Add line numbers to each line|line numbers, number lines"
    ["sort-lines"]="Sort Lines Alphabetically|Sort text lines alphabetically|sort lines, alphabetical sort"
    ["text-to-binary"]="Text to Binary|Convert text to binary code|text to binary, binary converter"
    ["binary-to-text"]="Binary to Text|Convert binary code to text|binary to text, binary decoder"
    ["text-to-hex"]="Text to Hex|Convert text to hexadecimal|text to hex, hex converter"
    ["hex-to-text"]="Hex to Text|Convert hexadecimal to text|hex to text, hex decoder"
    
    # 编码/解码类
    ["base64-encode"]="Base64 Encoder|Encode text to Base64|base64 encoder, base64 encode"
    ["base64-decode"]="Base64 Decoder|Decode Base64 to text|base64 decoder, base64 decode"
    ["url-encode"]="URL Encoder|Encode text for URLs|url encoder, percent encoding"
    ["url-decode"]="URL Decoder|Decode URL-encoded text|url decoder, percent decoding"
    ["html-encode"]="HTML Entity Encoder|Encode HTML entities|html encoder, html entities"
    ["html-decode"]="HTML Entity Decoder|Decode HTML entities|html decoder, html entities decoder"
    
    # JSON/代码类
    ["json-formatter"]="JSON Formatter|Format and validate JSON|json formatter, json validator, json beautifier"
    ["json-minifier"]="JSON Minifier|Minify JSON code|json minifier, json compressor"
    ["markdown-to-html"]="Markdown to HTML|Convert Markdown to HTML|markdown converter, markdown to html"
    ["html-to-markdown"]="HTML to Markdown|Convert HTML to Markdown|html to markdown, html converter"
    ["csv-to-json"]="CSV to JSON|Convert CSV to JSON format|csv to json, csv converter"
    ["json-to-csv"]="JSON to CSV|Convert JSON to CSV format|json to csv, json converter"
    
    # 其他实用工具
    ["diff-checker"]="Text Diff Checker|Compare two texts and find differences|text diff, diff checker, compare text"
    ["find-and-replace"]="Find and Replace|Find and replace text|find replace, search replace"
    ["text-to-speech"]="Text to Speech|Convert text to speech audio|text to speech, tts, speech synthesis"
    ["qr-code-generator"]="QR Code Generator|Generate QR codes from text|qr code generator, qr code maker"
    ["color-picker"]="Color Picker|Pick and convert colors|color picker, color converter, hex rgb"
    ["timestamp-converter"]="Unix Timestamp Converter|Convert Unix timestamps|timestamp converter, unix time"
    ["regex-tester"]="Regex Tester|Test regular expressions|regex tester, regex validator, regexp"
)

echo "工具总数: ${#tools[@]}"
for key in "${!tools[@]}"; do
    echo "$key"
done
