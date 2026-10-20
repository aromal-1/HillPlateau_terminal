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

Regenerate with:

```sh
python3 tapestry/faux_pi.py            # all scenes
python3 tapestry/faux_pi.py hill       # one of: curve, temple, hill, procession
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
```
