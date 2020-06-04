# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals


EXTENSIONS = {
    'adoc': {'text', 'asciidoc'},
    'asciidoc': {'text', 'asciidoc'},
    'apinotes': {'text', 'apinotes'},
    'asar': {'binary', 'asar'},
    'bash': {'text', 'shell', 'bash'},
    'bat': {'text', 'batch'},
    'bmp': {'binary', 'image', 'bitmap'},
    'bz2': {'binary', 'bzip2'},
    'c': {'text', 'c'},
    'cc': {'text', 'c++'},
    'cu': {'text', 'cuda'},
    'cfg': {'text'},
    'clj': {'text', 'clojure'},
    'cljc': {'text', 'clojure'},
    'cljs': {'text', 'clojure', 'clojurescript'},
    'cmake': {'text', 'cmake'},
    'cnf': {'text'},
    'coffee': {'text', 'coffee'},
    'conf': {'text'},
    'cpp': {'text', 'c++'},
    'crt': {'text', 'pem'},
    'cs': {'text', 'c#'},
    'csh': {'text', 'shell', 'csh'},
    'cson': {'text', 'cson'},
    'css': {'text', 'css'},
    'csv': {'text', 'csv'},
    'cxx': {'text', 'c++'},
    'dart': {'text', 'dart'},
    'def': {'text', 'def'},
    'dtd': {'text', 'dtd'},
    'ear': {'binary', 'zip', 'jar'},
    'edn': {'text', 'clojure', 'edn'},
    'ejs': {'text', 'ejs'},
    'eot': {'binary', 'eot'},
    'eps': {'binary', 'eps'},
    'erb': {'text', 'erb'},
    'exe': {'binary'},
    'eyaml': {'text', 'yaml'},
    'feature': {'text', 'gherkin'},
    'fish': {'text', 'fish'},
    'gemspec': {'text', 'ruby'},
    'gif': {'binary', 'image', 'gif'},
    'go': {'text', 'go'},
    'gotmpl': {'text', 'gotmpl'},
    'gpx': {'text', 'gpx', 'xml'},
    'graphql': {'text', 'graphql'},
    'gradle': {'text', 'groovy'},
    'groovy': {'text', 'groovy'},
    'gyb': {'text', 'gyb'},
    'gyp': {'text', 'gyp', 'python'},
    'gypi': {'text', 'gyp', 'python'},
    'gz': {'binary', 'gzip'},
    'h': {'text', 'header', 'c', 'c++'},
    'hpp': {'text', 'header', 'c++'},
    'htm': {'text', 'html'},
    'html': {'text', 'html'},
    'hxx': {'text', 'header', 'c++'},
    'icns': {'binary', 'icns'},
    'ico': {'binary', 'icon'},
    'ics': {'text', 'icalendar'},
    'idl': {'text', 'idl'},
    'idr': {'text', 'idris'},
    'inc': {'text', 'inc'},
    'ini': {'text', 'ini'},
    'j2': {'text', 'jinja'},
    'jade': {'text', 'jade'},
    'jar': {'binary', 'zip', 'jar'},
    'java': {'text', 'java'},
    'jenkinsfile': {'text', 'groovy'},
    'jinja': {'text', 'jinja'},
    'jinja2': {'text', 'jinja'},
    'jpeg': {'binary', 'image', 'jpeg'},
    'jpg': {'binary', 'image', 'jpeg'},
    'js': {'text', 'javascript'},
    'json': {'text', 'json'},
    'jsonnet': {'text', 'jsonnet'},
    'jsx': {'text', 'jsx'},
    'key': {'text', 'pem'},
    'kml': {'text', 'kml', 'xml'},
    'kt': {'text', 'kotlin'},
    'less': {'text', 'less'},
    'lidr': {'text', 'idris'},
    'lua': {'text', 'lua'},
    'm': {'text', 'c', 'objective-c'},
    'manifest': {'text', 'manifest'},
    'map': {'text', 'map'},
    'markdown': {'text', 'markdown'},
    'md': {'text', 'markdown'},
    'mib': {'text', 'mib'},
    'mk': {'text', 'makefile'},
    'ml': {'text', 'ocaml'},
    'mli': {'text', 'ocaml'},
    'mm': {'text', 'c++', 'objective-c++'},
    'modulemap': {'text', 'modulemap'},
    'ngdoc': {'text', 'ngdoc'},
    'nim': {'text', 'nim'},
    'nims': {'text', 'nim'},
    'nimble': {'text', 'nimble'},
    'nix': {'text', 'nix'},
    'otf': {'binary', 'otf'},
    'p12': {'binary', 'p12'},
    'patch': {'text', 'diff'},
    'pdf': {'binary', 'pdf'},
    'pem': {'text', 'pem'},
    'php': {'text', 'php'},
    'php4': {'text', 'php'},
    'php5': {'text', 'php'},
    'phtml': {'text', 'php'},
    'pl': {'text', 'perl'},
    'plantuml': {'text', 'plantuml'},
    'pm': {'text', 'perl'},
    'png': {'binary', 'image', 'png'},
    'po': {'text', 'pofile'},
    'pp': {'text', 'puppet'},
    'properties': {'text', 'java-properties'},
    'proto': {'text', 'proto'},
    'puml': {'text', 'plantuml'},
    'purs': {'text', 'purescript'},
    'py': {'text', 'python'},
    'pyi': {'text', 'pyi'},
    'pyx': {'text', 'cython'},
    'pxd': {'text', 'cython'},
    'pxi': {'text', 'cython'},
    'r': {'text', 'r'},
    'rb': {'text', 'ruby'},
    'rs': {'text', 'rust'},
    'rst': {'text', 'rst'},
    's': {'text', 'asm'},
    'sbt': {'text', 'sbt', 'scala'},
    'sc': {'text', 'scala'},
    'scala': {'text', 'scala'},
    'scss': {'text', 'scss'},
    'scm': {'text', 'scheme'},
    'sh': {'text', 'shell'},
    'sls': {'text', 'salt'},
    'so': {'binary'},
    'sol': {'text', 'solidity'},
    'spec': {'text', 'spec'},
    'ss': {'text', 'scheme'},
    'styl': {'text', 'stylus'},
    'sql': {'text', 'sql'},
    'svg': {'text', 'image', 'svg'},
    'swf': {'binary', 'swf'},
    'swift': {'text', 'swift'},
    'swiftdeps': {'text', 'swiftdeps'},
    'tac': {'text', 'twisted', 'python'},
    'tar': {'binary', 'tar'},
    'tgz': {'binary', 'gzip'},
    'thrift': {'text', 'thrift'},
    'tiff': {'binary', 'image', 'tiff'},
    'toml': {'text', 'toml'},
    'tf': {'text', 'terraform'},
    'tfvars': {'text', 'terraform'},
    'ts': {'text', 'ts'},
    'tsx': {'text', 'tsx'},
    'ttf': {'binary', 'ttf'},
    'txt': {'text', 'plain-text'},
    'vdx': {'text', 'vdx'},
    'vim': {'text', 'vim'},
    'vue': {'text', 'vue'},
    'war': {'binary', 'zip', 'jar'},
    'wav': {'binary', 'audio', 'wav'},
    'wkt': {'text', 'wkt'},
    'whl': {'binary', 'wheel', 'zip'},
    'woff': {'binary', 'woff'},
    'woff2': {'binary', 'woff2'},
    'wsgi': {'text', 'wsgi', 'python'},
    'xml': {'text', 'xml'},
    'xq': {'text', 'xquery'},
    'xql': {'text', 'xquery'},
    'xqm': {'text', 'xquery'},
    'xqu': {'text', 'xquery'},
    'xquery': {'text', 'xquery'},
    'xqy': {'text', 'xquery'},
    'xsd': {'text', 'xml', 'xsd'},
    'xsl': {'text', 'xml', 'xsl'},
    'yaml': {'text', 'yaml'},
    'yang': {'text', 'yang'},
    'yin': {'text', 'xml', 'yin'},
    'yml': {'text', 'yaml'},
    'zig': {'text', 'zig'},
    'zip': {'binary', 'zip'},
    'zsh': {'text', 'shell', 'zsh'},
}
EXTENSIONS_NEED_BINARY_CHECK = {
    'plist': {'plist'},
}

NAMES = {
    '.babelrc': EXTENSIONS['json'] | {'babelrc'},
    '.bashrc': EXTENSIONS['bash'],
    '.bash_aliases': EXTENSIONS['bash'],
    '.bash_profile': EXTENSIONS['bash'],
    '.bowerrc': EXTENSIONS['json'] | {'bowerrc'},
    '.coveragerc': EXTENSIONS['ini'] | {'coveragerc'},
    '.cshrc': EXTENSIONS['csh'],
    '.dockerignore': {'text', 'dockerignore'},
    '.editorconfig': {'text', 'editorconfig'},
    '.gitconfig': EXTENSIONS['ini'] | {'gitconfig'},
    '.hgrc': EXTENSIONS['ini'] | {'hgrc'},
    '.gitattributes': {'text', 'gitattributes'},
    '.gitignore': {'text', 'gitignore'},
    '.gitmodules': {'text', 'gitmodules'},
    '.jshintrc': EXTENSIONS['json'] | {'jshintrc'},
    '.mailmap': {'text', 'mailmap'},
    '.mention-bot': EXTENSIONS['json'] | {'mention-bot'},
    '.npmignore': {'text', 'npmignore'},
    '.pdbrc': EXTENSIONS['py'] | {'pdbrc'},
    '.pypirc': EXTENSIONS['ini'] | {'pypirc'},
    '.yamllint': EXTENSIONS['yaml'] | {'yamllint'},
    '.zshrc': EXTENSIONS['zsh'],
    'AUTHORS': EXTENSIONS['txt'],
    'BUILD.bazel': {'text', 'bazel'},
    'BUILD': {'text', 'bazel'},
    'CMakeLists.txt': EXTENSIONS['cmake'],
    'COPYING': EXTENSIONS['txt'],
    'Dockerfile': {'text', 'dockerfile'},
    'Gemfile': EXTENSIONS['rb'],
    'Jenkinsfile': {'text', 'groovy'},
    'LICENSE': EXTENSIONS['txt'],
    'MAINTAINERS': EXTENSIONS['txt'],
    'Makefile': EXTENSIONS['mk'],
    'NOTICE': EXTENSIONS['txt'],
    'PATENTS': EXTENSIONS['txt'],
    'Pipfile': EXTENSIONS['toml'],
    'Pipfile.lock': EXTENSIONS['json'],
    'README': EXTENSIONS['txt'],
    'Rakefile': EXTENSIONS['rb'],
    'setup.cfg': EXTENSIONS['ini'],
}
