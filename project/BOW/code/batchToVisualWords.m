function batchToVisualWords() 



%load the files and texton dictionary
load('../data/traintest.mat','all_imagenames','mapping');
load('dictionary.mat','filterBank','dictionary');

source = '';
target = ''; 

if ~exist(target,'dir')
    mkdir(target);
end

%{
for category = mapping
    if ~exist([target,category{1}],'dir')
        mkdir([target,category{1}]);
    end
end
%}

%This is a peculiarity of loading inside of a function with parfor. We need to 
%tell MATLAB that these variables exist and should be passed to worker pools.
filterBank = filterBank;
dictionary = dictionary;

%matlab can't save/load inside parfor; accumulate
%them and then do batch save
all_imagenames = all_imagenames{1,1};

l = length(all_imagenames);

wordRepresentation = cell(l,1);
count = 0
for i=1:l
    fprintf('Converting to visual words %d\n',i);
    pth = [source, all_imagenames{i,1}]
    image = imread(pth);
    pth
    wordRepresentation{i} = getVisualWords(image, filterBank, dictionary);
    count = count + 1
end

%dump the files
fprintf('Dumping the files\n');
for i=1:l
    wordMap = wordRepresentation{i};
    save([target, strrep(strrep(all_imagenames{i},'.jpg','.mat'), '.JPG', '.mat')],'wordMap');
end


end
