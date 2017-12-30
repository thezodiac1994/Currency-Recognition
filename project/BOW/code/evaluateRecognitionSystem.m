function [conf] = evaluateRecognitionSystem()
% Evaluates the recognition system for all test-images and returns the confusion matrix

	load('vision.mat');
	load('../data/traintest.mat');

	% TODO Implement your code here
    maps = string(zeros(1,size(mapping,2)));
    for i = 1 : 12 
        maps(1,i) = mapping{1,1} {1,i}; 
    end
conf = zeros(12,12);
for i = 1:size(test_imagenames{1,1},1)
    pth = test_imagenames{1,1}{i,1};
    pth = strcat(pth);
    predicted = guessImage(pth);
    actual = str2num(test_labels{1,1}{i,1});
    fprintf ('i = %d | a,p =  %d,%d\n',i,actual,predicted);
    conf(actual,predicted) = conf(actual,predicted) + 1;
end
    %display(conf);
    dlmwrite('myFile.txt',conf);
    percent = trace(conf) / sum (conf(:));
    percent*100
    
end