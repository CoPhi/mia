#!/usr/bin/env python3

from lxml import etree
import re

in_file_name = 'pagliara-output.xml'
out_file_name = 'pagliara-tokenized.xml'

tree = etree.parse(in_file_name)
root = tree.getroot()
ns = {'tei': 'http://www.tei-c.org/ns/1.0'}
#print('<doc>\n')
ab_elements = root.xpath('//tei:ab', namespaces=ns)
ab_contents_as_strings = []
for ab_element in ab_elements:
    w_n=0
    ab_type=ab_element.attrib['type']
    ab_n=ab_element.attrib['n']
    ab_str=f'<ab xmlns="http://www.tei-c.org/ns/1.0" type="{ab_type}" n="{ab_n}">\n'
    #ab_content = ''.join([etree.tostring(child, encoding='unicode', with_tail=True) for child in ab_element])
    ab_content=etree.tostring(ab_element,encoding="unicode")
    ab_content=re.sub(r'^<ab[^>]+>',r'',ab_content)
    ab_content=re.sub(r'</ab>',r'',ab_content)
    ab_content = ab_content.strip()
    ab_content = re.sub(r'xmlns="http://www.tei-c.org/ns/1.0" *',r'',ab_content)
    ab_content = re.sub(r' *>',r'>', ab_content)
    ab_content = re.sub(r'> *</abbr>', r'></abbr>', ab_content)
    ab_content = re.sub(r' type="',r'_type="', ab_content)
    ab_content = re.sub(r' rend="',r'_rend="', ab_content)
    ab_content = re.sub(r' ([·:|¶]+)',r'_\1',ab_content)
    ab_content = re.sub(r' ',r'\n', ab_content)
    ab_content = re.sub(r'(_*)(\|\||\|)',r'<seg_type="el">\1\2</seg>', ab_content)
    ab_content = re.sub(r'(_*)([·:¶,.]+)', r'<pc>\1\2</pc>', ab_content)
    ab_content = re.sub(r'_',r' ',ab_content)
    ab_content_tokens = ab_content.split('\n')
    for ab_content_token in ab_content_tokens:
        clean_token = re.sub(r'<[\u0000-\u00ff]*>', r'', ab_content_token)
        if(clean_token!=''):
            w_n+=1
            m_str=f'<milestone xml:id="{ab_type}-{ab_n}-{w_n}" unit="{ab_type}-tk" ana="{clean_token}"/>\n'
        else:
            m_str=''
        ab_str=''.join([ab_str,m_str, ' ', ab_content_token,'\n'])
    ab_str=''.join([ab_str,'</ab>'])
    new_ab_element=etree.fromstring(ab_str)
    ab_parent=ab_element.getparent()
    ab_parent.replace(ab_element,new_ab_element)
with open(out_file_name, 'w', encoding='UTF-8') as out_file:
    out_file.write(etree.tostring(root, pretty_print=True, encoding="unicode"))
