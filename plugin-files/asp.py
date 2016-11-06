#!/usr/bin/python2.7
#coding:utf-8

import re

#rule = '((?:eval|eval_r|execute|ExecuteGlobal)\s*?\(?request)'
rulelist = [
  '(\$_(GET|POST|REQUEST)\[.{0,15}\]\(\$_(GET|POST|REQUEST)\[.{0,15}\]\))',
  '(base64_decode\([\'"][\w\+/=]{200,}[\'"]\))',
  'eval\(base64_decode\(',
  '(eval\(\$_(POST|GET|REQUEST)\[.{0,15}\]\))',
  '(assert\(\$_(POST|GET|REQUEST)\[.{0,15}\]\))',
  '(\$[\w_]{0,15}\(\$_(POST|GET|REQUEST)\[.{0,15}\]\))',
  '(wscript\.shell)',
  '(gethostbyname\()',
  '(cmd\.exe)',
  '(shell\.application)',
  '(documents\s+and\s+settings)',
  '(system32)',
  '(serv-u)',
  '(提权)',
  '(phpspy)',
  '(后门)',
  '(webshell)',
  '(Program\s+Files)',
  'www.phpdp.com',
  'phpdp',
  'PHP神盾',
  'decryption',
  'Ca3tie1',
  'GIF89a',
  'IKFBILUvM0VCJD\/APDolOjtW0tgeKAwA',
  '\'e\'\.\'v\'\.\'a\'\.\'l\'',
  'cha88\.cn',
  'c99shell',
  'phpspy',
  'Scanners',
  'cmd\.php',
  'str_rot13',
  'webshell',
  '$fp = fsockopen',
  'EgY_SpIdEr',
  'tools88\.com',
  'SECFORCE',
 # 'eval\((\'|")\?>',
  'system\(',
  'passthru\(',
  'shell_exec\(',
  'exec\(',
  'popen\(',
  'proc_open',
 # 'eval\((\'|"|\s*)\\$',
  'assert\((\'|"|\s*)\\$',
  'returnsstringsoname',
  'intooutfile',
  'select(\s+)(.*)load_file',
  'eval\(gzinflate\(',
  'eval\(base64_decode\(',
  'eval\(gzuncompress\(',
  'eval\(gzdecode\(',
  'eval\(str_rot13\(',
  'gzuncompress\(base64_decode\(',
  'base64_decode\(gzuncompress\(',
  'eval\((\'|"|\s*)\\$_(POST|GET|REQUEST|COOKIE)',
  'assert\((\'|"|\s*)\\$_(POST|GET|REQUEST|COOKIE)',
  'require\((\'|"|\s*)\\$_(POST|GET|REQUEST|COOKIE)',
  'require_once\((\'|"|\s*)\\$_(POST|GET|REQUEST|COOKIE)',
  'include\((\'|"|\s*)\\$_(POST|GET|REQUEST|COOKIE)',
  'include_once\((\'|"|\s*)\\$_(POST|GET|REQUEST|COOKIE)',
  'call_user_func\(("|\')assert("|\')',
  'call_user_func\((\'|"|\s*)\\$_(POST|GET|REQUEST|COOKIE)',
  '\$_(POST|GET|REQUEST|COOKIE)\[([^\]]+)\]\((\'|"|\s*)\\$_(POST|GET|REQUEST|COOKIE)\[',
  'echo\(file_get_contents\((\'|"|\s*)\\$_(POST|GET|REQUEST|COOKIE)',
  'file_put_contents\((\'|"|\s*)\\$_(POST|GET|REQUEST|COOKIE)\[([^\]]+)\],(\'|"|\s*)\\$_(POST|GET|REQUEST|COOKIE)',
  'fputs\(fopen\((.+),(\'|")w(\'|")\),(\'|"|\s*)\\$_(POST|GET|REQUEST|COOKIE)\[',
  'SetHandlerapplication\/x-httpd-php',
  'php_valueauto_prepend_file',
  'php_valueauto_append_file'
  '((?:eval|eval_r|execute|ExecuteGlobal)\s*?\(?request)'
  '(shell_exec|execute|request|base64_decode|eval|%>|\$\w*\(\);)'
]


#        '(\<\%(\s|\n)*execute(\s|\n)*request\(.{0,15}\)\%\>)',
#        '(\<\%(\s|\n)*eval(\s|\n)*request\(.{0,15}\)\%\>)',
#        '(\<\%(\s|\n)*eval_r(\s|\n)*(R|r)equest.(I|i)tem\[.{0,15}\],.{0,15}(\s|\n)*;(\s|\n)*\%\>)'
def Check(filestr,filepath):
    for rule in rulelist:
        result = re.compile(rule).findall(filestr)
        if len(result)>0:
            return result,'发现后门'
    return None
