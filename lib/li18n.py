import os, gettext

from utils.cfiles import full_dir

localedir = os.path.join(full_dir(__file__), '..', 'locale')
translate = gettext.translation('li18n', localedir, languages=['en'], fallback=True)
_ = translate.gettext

text = _('Estoy en casa de {name} en la {number} planta').format(name='Juan', number='3ª')

print(text)


# Create .pot file (template of .po) getting _('') string from indicated file
# pygettext -o locale/en/LC_MESSAGES/li18n.pot lib/li18n.py

# .po to .mo
# msgfmt -o locale/en/LC_MESSAGES/li18n.mo locale/en/LC_MESSAGES/li18n.po