let sentence = "The movie is not that bad, I like it";
let wordNot = sentence.indexOf("not");
let wordBad = sentence.indexOf("bad");

if (wordNot !== -1 && wordBad !== -1 && wordBad > wordNot) {
    let before = sentence.slice(0, wordNot);
    let after = sentence.slice(wordBad + 3);
    let newSentence = before + "good" + after;
    console.log(newSentence);
} else {
    console.log(sentence);
}
