clear all;
clc;

filename = 'Declaration_of_Independance.txt';
fileID = fopen(filename,'r'); %Open File
if (fileID > 0) % check if the pipe opened correctly
    data = fscanf(fileID,'%c'); % Write file into a variable
    fclose(fileID); % Close the pipe
end
bin = dec2bin(data,8); % translate text to binary
filename = 'Declaration_of_Independance.txt';
fileID = fopen('binary_text.txt','w'); %Open File
if (fileID > 0) % check if the pipe opened correctly
    data = fprintf(fileID,'%s', bin); % Write file into a variable
    fclose(fileID); % Close the pipe
end