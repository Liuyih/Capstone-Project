# flake8: noqa

# Provided to CS16 on 2019 Nov 1
# Original script from Jessica Curtis:
# -------------------------------------------------------
# import modules used here -- sys is a very standard one
import sys
from datetime import datetime, date

print ('Program starting, filename is first arg (NOTE: must not have any blank spaces in name!)):', sys.argv[1])
d_filename=sys.argv[1] ; #print("File to read is: "+ d_filename)
idName, rej = d_filename.split(".")
outFile, ext = d_filename.split('.')
print("raw file name="+outFile)
outfileData=outFile+"Data_1.csv"
outfileHeader=outFile+"Header.csv"
outfileData=open(outfileData,'w')
outfileHeader=open(outfileHeader,'w')


header=0; cycleID=0; linecounter=0; writelinecounter=0; ADCcounter=0; EX1counter=0; mS1counter=0
detectorOn=0; detectorOff=0; mS0counter=0; writeLine=" "; foundheader=0;newline="";milliSec=" ";

with open(d_filename) as fp:
     for line in fp:
          linecounter +=1;
          if (header==0): outfileHeader.write(line)
          if 'Acq Start Reference' in line: header=1; 
          if (line.find('ADC:',0,len(line))>-1 and detectorOn==1 and line.find('Real:',0,len(line))>-1 and line.find('UTC Time:',0,len(line))>-1 ): 
               rej,newline=line.split('Real:');
               newline1,time=newline.split('UTC Time:');
               newline2,channel=newline1.split('ADC:');
               milliSec,rej=newline2.split('mS');

               #print(str(cycleID)+","+ milliSec +","+ channel +","+ time);
               writeLine=str(cycleID)+","+ milliSec +","+ channel +","+ time;

               #print(writeLine);
               outfileData.write(writeLine);

          if (line.find('EX1',0,len(line))>-1 and line.find("mS: 1",0,len(line))>-1 and detectorOff==1): 
               mS1counter +=1; detectorOn=1; detectorOff=0; cycleID +=1; 
               outfileData.close();
               outfileData=outFile+"Data_"+str(cycleID)+".csv";
               outfileData=open(outfileData,'w');
               outfileData.write("runID, millisec, Bin, timestamp \n");
               print("lines read so far: "+ str(linecounter)+ " ,last line of previous cycle: " + str(writeLine)+ "\n new cycle: "+ str(cycleID) + " line: "+ line);
          
          if (line.find('EX1',0,len(line))>-1 and line.find("mS: 0",0,len(line))>-1):
               mS0counter +=1; detectorOn=0; detectorOff=1; 
             
                                                            


print("cycleCounter:"+str(cycleID)+" linecounter: "+ str(linecounter) + " mS1counter:"+str(mS1counter))
# to see all millisec decimal places in R options(digits=10) and to load into R dataframe: filename<-read.csv("parsedFileName") 


          
     

     
