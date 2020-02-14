# Word Alignment

## IBM Model 1
- IBM Model is a Word Based Model for Machine Translation. It is a generative model.
- f: foreign language and e: english. We want to convert f->e
- Translation probability P(e|f) and Alignment function a(j) -> i are calculated using **Expectation Maximization** on sentence aligned text
- The Translation Probabilities are initialized uniformly as 1/size_of_vocabulary
- Counts of obtaining e given f are initialized to 0 and total number of times a word f occurs is initialized to 0 as well
- Now in every iteration, s-total(e) is calcualted which gives the expected number of times the word e has occurred in the corpus. Using this, count(e|f) and total(f) are re-calculated and then t(e|f) is calculated
- t(e|f) is stored using a dictionary => translation_prob {e1 : {f1 : p11, f2 : p12, ...}, e2 : {f1 : p21, f2 : p22, ...}, ... }. To save memory as well as computation, only those pairs (e,f) are included in the dictionary which have a probability of occurring 
- count(e|f) is stored in a similar manner as t(e|f). Rather than storing the counts of all pairs of (e,f), only those ones are stored which actually occur
- s-total(e) and total(f) are also dictionaries

### Results
##### English French Corpus
- **Precision** = 0.6748952929446704
- **Recall** = 0.5686194765008536
- **Alignment Error Rate** = 0.3861122636420051

Some of the alignments that IBM Model 1 gives (calculated based on highest translation probability) :
- Resumption Reprise 0.7256998771239865
- the la 0.6695349032190662
- session session 0.7000231087916889
- I j 0.9693147236602473
- declare interrompue 0.38103901156222214
- resumed reprise 0.4677492419509894
- European européen 0.9902584631623801
- Parliament Parlement 0.9872802316993381
- adjourned interrompue 0.5628864116710103
- of Pensons 0.4489238627265153
- observed Andrés 0.1906864317860294
- who Pristina 0.43998538902004225
- enjoyed Français 0.23148559917324313


##### English Hindi Corpus
Some of the alignments that IBM Model 1 gives (calculated based on highest translation probability) : 
- treatment उपचार 0.8901654774236055
- taken ली 0.35859244490666603
- out निकल 0.6009982616856768
- in मे 0.8517261817524703
- possible संभव 0.7831900106316432
- through जरिये 0.579377449504992
- surgery सर्जरी 0.9392532685323253
- Complete रज्जु 0.8071970634891557
- family परिवार 0.9081239727812345
- symptoms लक्षणों 0.8337196912704791
- iris आइरिस 0.18449954704953914
- frontal आइरिस 0.18447682997991557
- intact तरीक़ों 0.2552383172291497
- caused लूटपाट 0.22125332461222136
- somebody रुक-रुककर 0.24459669205291884 
