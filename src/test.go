package main

import (
	"fmt"
	"golang.org/x/net/html"
	"log"
	"os"
	"strings"
)

var startTag = map[string]string{
	"h1": `<h1 class="title">`,
	"h2": `<h2 class="title">`,
	"h3": `<h3 class="title">`,
}

var endTag = map[string]string{
	"h1": "</h1>",
	"h2": "</h2>",
	"h3": "</h3>",
}

func readHtmlFromFile(fileName string) (string, error) {
	bs, err := os.ReadFile(fileName)

	if err != nil {
		return "", err
	}

	return string(bs), nil
}

func parse(text string) string {
	tkn := html.NewTokenizer(strings.NewReader(text))

	var result string

	for {
		tt := tkn.Next()

		switch {
		case tt == html.ErrorToken:
			return result

		case tt == html.StartTagToken:
			tag := tkn.Token().String()
			tag = tag[1 : len(tag)-1]

			result += startTag[tag]

		case tt == html.TextToken:
			tag := tkn.Token().String()
			result += tag

		case tt == html.EndTagToken:
			tag := tkn.Token().String()
			tag = tag[2 : len(tag)-1]

			result += endTag[tag]
		}
	}
}

func main() {
	const fileName = "index.html"
	text, err := readHtmlFromFile(fileName)

	if err != nil {
		log.Fatal(err)
	}

	data := parse(text)
	fmt.Println(data)
}
