from rich.console import Console
from rich.text import Text

redder = "\033[38;2;243;99;46m"
console = Console(force_terminal=True)
text = Text()
red = "#f3632e"
# Append a raw string (r"…") to the Text object with a specific color style.
# The 'r' before the string makes it a raw string literal (backslashes are not treated as escape characters).
text.append("           ..                                                         ", style=red)
console.print(text)
print ("          .7!.                                                        ")
print ("               :^^.                                                   ")
print ("        ...    !7!.                                                   ")
print ("        ~7^        ^!!!:                                              ")
print ("            .^~^  .!!!~ :~~~~:                                        ")
print ("            ^!!:       .?JJJ7..^^^^^        .^~~~~^^^::.              ")
print ("                :!77~        :?JJJJ~       .7JJJJJJJJJJ!    ^^..      ")
print ("                ^~~~. ~!!!~                !J????????J7    ~??77!^.   ")
print ("   .::               ~????: ~!~~~:        !JJ???????J7.   ^777777?7!^.")
print ("   !7:               ....  !JJJJ7.       ~JJ???????J?.   :7777777777?~")
print ("       :!!^                :::::.       ^JJJJJJJJ?J?:   :7777777777?~ ")
print (".^^    ^!~:                            :777?????JJJ^   .7777777777?!  ")
print ("^!~        ^???~                              ..:^:    !??777777777.  ")
print ("     !7!.  :^^^.:????!               .........         .:~!77?7777.   ")
print ("    .~~^  ...   !???7..77777:       .?JJJJJJJJ??^    .     .:~7?7:    ")
print ("        .?JJ?. ..    .?YYYY!        7YYYJJYYYYY?    ^~^^:.     ::     ")
print ("        .:::. 7JJJ?:               !YJJJJJJJJY?.   :~~~~~~~^:         ")
print ("             :7777^ !????!        ~YJJJJJJJJYJ.   :~~~~~~~~~~~.       ")
print ("                   ~JJJJ?.       ^YYJJJJJJJYJ:   .~~~~~~~~~~~^        ")
print ("                   ......       ^YYYYYYYYYYY^   .~~~~~~~~~~~~         ")
print ("                                :~^~~!!77?J~   .~~~~~~~~~~~~.         ")
print ("                                          .    :~~~~~~~~~~~.          ")
print ("                                                 ..:^~~~~~:           ")
print ("                                                     ..^~:            ")
                                                                      
