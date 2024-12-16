**PYTHON SCRIPTS PACKAGE FOR Manuscripta Allographica Project**
The package aims to convert .docx files into xml-TEI. 
These scripts are tailored on greek alphabet to latin alphabet texts but the pack will be optimized for hebrew arabic-syriac texts. 

AUTHORS

Federico Boschetti, Giulia Re

CONTENTS

*1_installer*: installs py libraries, imports file path and imports Transcoder, opens renamed file.

*2_layout_creator*: opens the file and splits it into lines.

*3_determine_language*: Cases like {δ::L}, conventionally used to mark an expunction, generate ambiguity. This causes problems in assigning <grc> or <ita> to each paragraph. 
The code adopts milestones in order to minimize the impact of ambiguous cases, does a predominance count in order to assign language (if over 20% in the line). 

*4_tei_structure_creator*: structures the file according to xml-TEI layout conventions. 

*5_xml_formatting_&_refining*:  organizes and segments paragraph <p> (or <ab> when required), recalling 3_determine_language for the attribution of <gr> or <ita>. Refines and cleans the para_list.

*6_main_&_download_output*: calls the main function and downloads the TEI-xml output. 

*7_tokenizer*: The tokenizer is the preliminary step towards the many2many alignment, by transforming tei-xml outputs (cf. 6) into tokens. 
This code parses our outputs, cycles on the <ab> or <p> elements and their attributes (type and n) in order to build a new xml string for the new <ab> or <p> and attributes.
The content is then cleaned and splitted into a token list, cleaned of previous xml tags. 

*8_many2many_aligner*: 
