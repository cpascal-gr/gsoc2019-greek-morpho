# GSOC 2019 - Development of a Greek open source Morphological dictionary and application of it to Greek spelling tools

## Dictionary Download

The version v0.2 of the morphological dictionary can be found [here](data/morph-dict-v0.2.zip).

It contains about 518000 distinct surface forms and about 900000 forms with morphological information. 

The spelling dictionary is found [here](data/)

## Running the script

Information about running the script is found [here](doc/wiktionary_script.md)

## Project goals

During the summer a Morphological dictionary in sqlite3 format will be created.
Information will be extracted automatically with a python script and using
the pymediawiki library. In addition words and morphological information
will be added to the spelling tool dictionaries.

## Deliverables

1. A Morphological dictionary of Greek in SQLite3 format that includes complete morphology for 
 Nouns, Proper Nouns, Adjectives, Verbs, Prepositions, Adverbs, Acronyms
 with information automatically extracted from the Greek wiktionary
 using Universal Dependencies Tagset.
2. Addition of the extracted words to open source spelling dictionaries.

## Final Report

You can find the final report in the following [gist](https://gist.github.com/algorithm314/449e301c331c7d91a5116c0d00703a20).

## Timeline

### Phase 1 (May 27 - Jun 28)

Creation of a parsing tool for Greek wiktionary that parses nouns, adjectives, verbs using Universal Dependencies POS tags

### Phase 2 (Jun 29 - Jul 26)

Addition of remaining parts of speech to the Morphological dictionary and
 addition of further information tags like toponyms and terminology extracted from page categories.

### Phase 3 (Jul 27 - Aug 26)

 Addition of extracted surface forms to Greek spelling dictionaries including words from reliable sources like European parliament translations.

## Contributors

* Google summer of code participant: Konstantinos Agiannis
* Mentor: Kostas Papadimas
* Mentor: Diomidis Spinellis
* Mentor: Alexios Zavras


## License

The source code is under GPLv3.

The produced database with the morphological dictionary is under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

## Links

 * [Greek Wiktionary](https://el.wiktionary.org/)
 * [hunspell documentation](https://www.systutorials.com/docs/linux/man/4-hunspell/)
 * [UD\_GREEK-GDT](https://github.com/UniversalDependencies/UD_Greek-GDT/)
 * [Tagset Greek](http://nlp.ilsp.gr/nlp/tagset_examples/tagset_el/)
 * [Fast Tokenizer](https://github.com/algorithm314/fast-tokenizer)
