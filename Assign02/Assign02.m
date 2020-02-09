clear all;
clc;

filename = 'Assign02/Declaration_of_Independance.txt';
fileID = fopen(filename,'r'); %Open File
if (fileID > 0) % check if the pipe opened correctly
    data = fscanf(fileID,'%c'); % Write file into a variable
    fclose(fileID); % Close the pipe
end
bin = dec2bin(data,8); % translate text to binary
fileID = fopen('Assign02/binary_text_matlab.txt','w'); %Open File
if (fileID > 0) % check if the pipe opened correctly
    fprintf(fileID,'%c', bin'); % Write file into a variable
    fclose(fileID); % Close the pipe
end