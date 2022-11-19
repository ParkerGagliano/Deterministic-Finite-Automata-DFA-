# Deterministic Finite Automata - DFA

This program creates DFA trees based on DFA descriptions and accepts or denies binary strings, either single input or file input

This was created with a simple DFA in mind as pictured:  
![image](https://user-images.githubusercontent.com/20826285/202829679-9bd874bb-71e1-47d6-91ab-5a1c5b6309ca.png)

## Using this program

1. Run main, and input the details of the DFA you want to recreate, starting with all the states, the picture above has q0 q1 q2
   and you would input it exactly the same <br /><br />
   `q q1 q2` <br /><br />
2. Then answer if you're using a file as input, if you are, you must place the text file in the same directory as main
   `y` or `n`<br /><br />
3. Then following the mathmetical way to represent one as pictured here answer all the mapping questions<br /><br />
   ![image](https://user-images.githubusercontent.com/20826285/202830021-8aa30964-8f09-4eee-abef-fdbe22a9eac2.png)<br /><br />
   Answering with <br /><br />
   `q0` or `q1` or `q2`<br /><br />
4. Then, use the same inputs to specify the initial and final states<br /><br />
5. If you specified a file input, you must input the filename exactly with the .txt extension as well<br /><br />
6. Lastly, specify the string you want to try putting through the DFA, EX `101010101010110` and choose if you want to see it evaluate while printing its progress or not
   <br /><br />
   if you chose file input, a new text file will appear in the same directory as main with all the accepted strings
