import blessed
term = blessed.Terminal()

print(term.on_green('This will not standout on a vt220'))
print(term.green_reverse('Though some terminals standout more than others'))
#print(term.peru_on_seagreen('All syst        🐇 🐺 👤 α Ω       arameters.'))
print(term.white_on_seagreen('🐇 🐺 👤 α Ω'))
print(term.black_on_seagreen('🐇 🐺 👤 α Ω'))
print(term.underline_bold_red_on_seagreen('🐇 🐺 👤 α Ω'))
