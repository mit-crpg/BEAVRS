#!/usr/bin/env gnuplot

set terminal pdf enhanced
set output 'boron_letdown.pdf'
set xlabel 'EFPD'
set ylabel 'Boron [ppm]'
plot '-' using 1:2 with linespoints ps 1 pt 7 lw 2 lc rgb 'red' title 'Cycle 1', \
     '-' using 1:2 with linespoints ps 1 pt 9 lw 2 lc rgb 'blue' title 'Cycle 2'
4 599
11 610
16 614
22 621
31 638
36 610
52 623
69 598
85 569
96 559
110 533
124 506
141 471
144 461
152 457
164 415
174 394
177 384
180 384
190 367
204 322
214 296
219 286
225 270
228 270
248 207
271 149
295 72
326 0
e
13 918
23 882
43 832
63 764
84 687
103 623
129 538
150 466
176 376
202 292
234 184
257 104
e
