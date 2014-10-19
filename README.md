SublimeLinter for Sublime Text 2 PHPCF Module
=============================================


Copy phpcf.py into SublimeLinter Module directory:

<code>
Packages/SublimeLinter/sublimelinter/modules
</code>

Add phpcf in sublimelinter_executable_map and sublimelinter_syntax_map of SublimeLinter User Settings:

    "sublimelinter_executable_map":
    {
        "php": "/usr/bin/php",
        "phpcf": "/usr/bin/phpcf"
    }

    "sublimelinter_syntax_map":
    {
        "Python Django": "python",
        "Ruby on Rails": "ruby",
        "C++": "c",
        "PHP": "phpcf"
    }

Done.
