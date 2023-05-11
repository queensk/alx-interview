# 0x03. Log Parsing

## Script for Computing Metrics from Stdin

This script reads input from the standard input (stdin) line by line and computes metrics based on the provided input format. It calculates the total file size and counts the number of lines for each status code. The statistics are printed after every 10 lines or when a keyboard interruption (CTRL + C) occurs.

## Input Format
The input should follow the format:
```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```
If the input line does not match this format, it will be skipped.

## Usage
To use the script, you can pipe the input from another script or file into it. For example:

```
./generator.py | ./stats.py
```
## Metrics
The script computes the following metrics:

## Total File Size
The total file size is the sum of all previous file sizes encountered in the input. After every 10 lines or a keyboard interruption, the script prints:
`File size: <total size>`

## Number of Lines by Status Code
The script counts the number of lines for each status code encountered in the input. The possible status codes are:
```
200
301
400
401
403
404
405
500
```
If a status code doesn't appear or is not an integer, no output is printed for that status code. The status codes are printed in ascending order along with the count. The format is:
`<status code>: <number>`

Note: The status codes are based on the provided sample and may vary depending on the input.

## Example Output
The output will be displayed after every 10 lines or a keyboard interruption. Here's an example:
```
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
File size: 16305
200: 3
301: 3
400: 4
401: 2
403: 5
404: 5
405: 4
500: 4
```
Please note that the specific values will be random in each execution due to the nature of the provided sample.

This script provides a convenient way to process input data from stdin and compute metrics based on the specified format. Feel free to modify and adapt it to suit your specific needs.
