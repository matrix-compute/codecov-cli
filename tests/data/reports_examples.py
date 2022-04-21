"""This module defiens some reports examples that are going to be used by tests"""

# Avoid parsing and removing indentation from multiline strings by defining them in the top level of this file


coverage_file_section_simple = b"""# path=flagtwo.coverage.xml
<?xml version="1.0" ?>
<coverage branch-rate="0" branches-covered="0" branches-valid="0" complexity="0" line-rate="0.6" lines-covered="30" lines-valid="50" timestamp="1600652028856" version="4.5.4">
    <!-- Generated by coverage.py: https://coverage.readthedocs.io -->
    <!-- Based on https://raw.githubusercontent.com/cobertura/web/master/htdocs/xml/coverage-04.dtd -->
    <sources>
        <source>/Users/thiagorramos/Projects/clientenv/example-python</source>
    </sources>
    <packages>
        <package branch-rate="0" complexity="0" line-rate="0.68" name="awesome">
            <classes>
                <class branch-rate="0" complexity="0" filename="awesome/__init__.py" line-rate="0.6471" name="__init__.py">
                    <methods/>
                    <lines>
                        <line hits="1" number="1"/>
                    </lines>
                </class>
                <class branch-rate="0" complexity="0" filename="awesome/code_fib.py" line-rate="0.75" name="code_fib.py">
                    <methods/>
                    <lines>
                        <line hits="1" number="1"/>
                    </lines>
                </class>
            </classes>
        </package>
        <package branch-rate="0" complexity="0" line-rate="0.52" name="tests">
            <classes>
                <class branch-rate="0" complexity="0" filename="tests/__init__.py" line-rate="1" name="__init__.py">
                    <methods/>
                    <lines/>
                </class>
                <class branch-rate="0" complexity="0" filename="tests/test_number_two.py" line-rate="0" name="test_number_two.py">
                    <methods/>
                    <lines>
                        <line hits="0" number="1"/>
                    </lines>
                </class>
                <class branch-rate="0" complexity="0" filename="tests/test_sample.py" line-rate="1" name="test_sample.py">
                    <methods/>
                    <lines>
                        <line hits="1" number="1"/>
                    </lines>
                </class>
            </classes>
        </package>
    </packages>
</coverage>
<<<<<< EOF
"""

coverage_file_section_small = b"""# path=unit.coverage.xml
<?xml version="1.0" ?>
<coverage branch-rate="0" branches-covered="0">
    <packages>
    </packages>
</coverage>
<<<<<< EOF
"""


env_section = b"""PRODUCTION_TOKEN=aaaaaaaa-e799-40d4-b89d-cea4b18f29a4
<<<<<< ENV
"""

network_section = b"""./codecov.yaml
Makefile
awesome/__init__.py
awesome/code_fib.py
dev.sh
tests/__init__.py
tests/test_number_two.py
tests/test_sample.py
unit.coverage.xml
<<<<<< network
"""



env_network_coverage_sections = b"""PRODUCTION_TOKEN=aaaaaaaa-e799-40d4-b89d-cea4b18f29a4
<<<<<< ENV
./codecov.yaml
Makefile
awesome/__init__.py
awesome/code_fib.py
dev.sh
tests/__init__.py
tests/test_number_two.py
tests/test_sample.py
unit.coverage.xml
<<<<<< network
# path=flagtwo.coverage.xml
<?xml version="1.0" ?>
<coverage branch-rate="0" branches-covered="0" branches-valid="0" complexity="0" line-rate="0.6" lines-covered="30" lines-valid="50" timestamp="1600652028856" version="4.5.4">
    <!-- Generated by coverage.py: https://coverage.readthedocs.io -->
    <!-- Based on https://raw.githubusercontent.com/cobertura/web/master/htdocs/xml/coverage-04.dtd -->
    <sources>
        <source>/Users/thiagorramos/Projects/clientenv/example-python</source>
    </sources>
    <packages>
        <package branch-rate="0" complexity="0" line-rate="0.68" name="awesome">
            <classes>
                <class branch-rate="0" complexity="0" filename="awesome/__init__.py" line-rate="0.6471" name="__init__.py">
                    <methods/>
                    <lines>
                        <line hits="1" number="1"/>
                    </lines>
                </class>
                <class branch-rate="0" complexity="0" filename="awesome/code_fib.py" line-rate="0.75" name="code_fib.py">
                    <methods/>
                    <lines>
                        <line hits="1" number="1"/>
                    </lines>
                </class>
            </classes>
        </package>
        <package branch-rate="0" complexity="0" line-rate="0.52" name="tests">
            <classes>
                <class branch-rate="0" complexity="0" filename="tests/__init__.py" line-rate="1" name="__init__.py">
                    <methods/>
                    <lines/>
                </class>
                <class branch-rate="0" complexity="0" filename="tests/test_number_two.py" line-rate="0" name="test_number_two.py">
                    <methods/>
                    <lines>
                        <line hits="0" number="1"/>
                    </lines>
                </class>
                <class branch-rate="0" complexity="0" filename="tests/test_sample.py" line-rate="1" name="test_sample.py">
                    <methods/>
                    <lines>
                        <line hits="1" number="1"/>
                    </lines>
                </class>
            </classes>
        </package>
    </packages>
</coverage>
<<<<<< EOF
"""