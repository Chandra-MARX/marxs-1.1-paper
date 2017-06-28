# marxs-1.1-paper

This is the source code for the MARXS 1.1 paper including the tex source
(for use with pdflatex), the bbl file, and the plot scripts.

## Need dev version to run examples

You need the current development version of MARXS to run the plot scripts,
not (as the article indicates) the released version. I will release version
1.1 just before I submit this paper top bring that back in sync, but I want to
delay that release as much as possible, to include any bugs that might turn up
while preparing this paper.

## Plot scripts differ from MARXS docs

Plot scripts differ from the examples in the documentation. I will prot them 
back to the sphinx docs in marxs just before submission to match in the 
1.1 release (except for trivial formatting like font sizes because the format
of the plots is different in the documentation from the layout of a journal 
paper).

## bibtex

I use bibtex for references, but I inlcude the bbl file in this repro, not the
bibfile. I use a large .bib file that includes many refernces unrelated to
this paper and I don't want ot clutter the repro with it.
You can run pdflatex with the bbl file, please let me know if you add any
references to the article and I'll update my (local) master bib file.
