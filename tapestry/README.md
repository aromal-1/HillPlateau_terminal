# tapestry: reformations of `mount_tapestry`

The source is [`mount_tapestry`](https://github.com/MONASTERY-DENUMERATIONS/HillPlateau_terminal/blob/main/mount_tapestry)
in MONASTERY-DENUMERATIONS/HillPlateau_terminal.

## What the file is

It's an ASCII elevation of a temple standing on a hill. From top to bottom:

| Rows in `mount_tapestry` | What they draw |
|---|---|
| `˜ˀ-0.1f`, `\|\|\|\|\|\|` | finial and spire |
| `/////\|\\\\\`, `(((++++)))` | tiered roof over the shrine |
| `IIII…`, `\| \| \| \|` | lintel and colonnade |
| `[][][]`, `{__}{__}` | lattice screen and plinth |
| `>>>><<<<`, `§§§ \|=\|=\| §§§` | stairway and gate posts |
| `(((––––)))`, `/////   \\\\\` | terraces and the slopes of the mount |

So the title "HillPlateau" fits: a temple sits on a plateau, and every route goes *up*.

## `faux(pi, x)`

`faux(pi, x)` is a "fake pi". It's the Leibniz partial sum `4 · Σ (-1)^k / (2k+1)` over `x` terms.
Odd `x` overshoots π and even `x` undershoots it, so the sum zig-zags toward π the way a switchback
path climbs to a temple. Every scene below is built from it:

- **curve**: the zig-zag itself, settling onto the line `pi`.
- **temple**: `mount_tapestry` reformed at a small size.
- **hill**: a plateau hill whose terraces step by `faux(pi, x) - pi`. Ministers climb toward the temple;
  the ones lower down haven't found a pot yet (`o?`), and the higher ones carry one (`(_)`).
- **procession**: ministers queue at the gate. Minister `x` carries a pot when `faux(pi, x) > pi`.
- **cavern**: pixel coverage of the rock under the hill, shaded with ` .:-=+*#%@` from hollow to solid.
  The edge of the hollow wobbles by `faux(pi, x) - pi`, and a minister finds a pot inside.
- **castle**: a castle of width Infinity. `castle_columns()` is an endless generator: it puts a tower
  wherever `faux(pi, x) > pi` and a wall between towers. The scene crops it to the terminal width.
- **chant**: "realm of existence" chanted along a rod in every tense (past, present, plus-future).
  Each echo is fainter than the one before.

Regenerate with:

```sh
python3 tapestry/faux_pi.py            # all scenes
python3 tapestry/faux_pi.py hill       # one of: curve, temple, hill, procession, cavern, castle, chant
```

## Output

```text
faux(pi, x): odd x overshoots (*), even x undershoots (o)
4.0     *





            *
                *   *
                        *   *   *   *   *   *   *   *   *   *   *   *   *   *
pi      --------------------------o---o---o---o---o---o---o---o---o---o---o---o-*-o-*-o-
                  o   o   o   o
              o

2.67      o

        +-------------------------------------------------------------------------------
        x=1                                                                       x=40

mount_tapestry, reformed small
         ˀ         
        |||        
   /////|||\\\\\   
   \-----------/   
    |(((+++)))|    
 IIIIIIIIIIIIIIIII 
  | | | | | | | |  
 /_______________\ 
 |IIIIIIIIIIIIIII| 
 |  ===========  | 
 [][][][][][][][][]

Visiting the temple: ministers climbing faux(pi, x) hill
                                       ˀ
                                      |||
                                 /////|||\\\\\
                                 \-----------/
                                  |(((+++)))|
                               IIIIIIIIIIIIIIIII
                                | | | | | | | |
                         (_)   /_______________\
                         \o/   |IIIIIIIIIIIIIII|
                   (_)    |    |  ===========  |
                   \o/   / \   [][][][][][][][][]
                    |    /____________________________
              o?   / \ /_      .          .          .\_
             /|\   /___      .          .          .    \___
             / \ /_        .          .          .          \_
        o?    /__        .          .          .          .   \__
       /|\   /         .          .          .          .        \
       / \/__        .          .          .          .          .\__
         /         .          .          .          .          .     \
       /_        .          .          .          .          .        \_
     /_        .          .          .          .          .          . \_
   /_        .          .          .          .          .          .     \_
  /        .          .          .          .          .          .         \
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Procession to the gate
(_)         (_)         (_)           §§|§§
\o/    o?   \o/    o?   \o/    o?     |===|
 |    /|\    |    /|\    |    /|\     |   |
/ \   / \   / \   / \   / \   / \   __|   |__
x where faux(pi, x) > pi carries a pot; the rest are still trying to get one

Cavern: pixel coverage of rock, @ is solid, blank is hollow
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%@@@@@%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@##*@@++=@@@:::@@@@@:::@@@=++@@*##@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@%%@@@+==**+:..==   ---   *****   ---   ==..:+**==+@@@%%@@@@@@@@@@@
@@@@@@@%#@%#=-+==.  ..                                   ..  .==+-=#%@#%@@@@@@
@@@@@@*+=+==. ..                                               .. .==+=+*@@@@@
@@%@%#=-:-:.                       (_)                             .:-:-=#%@%@
@%#%#*--:::.                       \o/ (_)                         .:::--*#%#%
@@%@%#=-:-:.                        |                              .:-:-=#%@%@
@@@@@@*+=+==. ..                   / \                         .. .==+=+*@@@@@
@@@@@@@%#@%#=-+==.  ..                                   ..  .==+-=#%@#%@@@@@@
@@@@@@@@@@@@%%@@@+==**+:..==   ---   *****   ---   ==..:+**==+@@@%%@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@##*@@++=@@@:::@@@@@:::@@@=++@@*##@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%@@@@@%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
a minister has found a pot hidden in the cavern

Castle of width Infinity: towers where faux(pi, x) > pi, walls between
[]_[]_[]       []_[]_[]       []_[]_[]       []_[]_[]       []_[]_[]      
|  ..  |_[]_[]_|  ..  |_[]_[]_|  ..  |_[]_[]_|  ..  |_[]_[]_|  ..  |_[]_[]
|  []  |  : :  |  []  |  : :  |  []  |  : :  |  []  |  : :  |  []  |  : : 
|      |       |      |       |      |       |      |       |      |       ...
|  /\  |  : :  |  /\  |  : :  |  /\  |  : :  |  /\  |  : :  |  /\  |  : : 
|_|  |_|_______|_|  |_|_______|_|  |_|_______|_|  |_|_______|_|  |_|______
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
(an endless generator, cropped to 78 columns)

Chant along the rod: all tenses, each echo fainter
  ||  [past]
  ||  @@ was the realm of existence
  ||  %%   was the realm of existence
  ||  ##     was the realm of existence
  ||  **       was the realm of existence
  ||  [present]
  ||  @@ is the realm of existence
  ||  %%   is the realm of existence
  ||  ##     is the realm of existence
  ||  **       is the realm of existence
  ||  [plus-future]
  ||  @@ will have been the realm of existence
  ||  %%   will have been the realm of existence
  ||  ##     will have been the realm of existence
  ||  **       will have been the realm of existence
 _||_
|____|  Dev.rod(map.schema): each tense maps one band of the rod
```
