function buildRecognitionSystem()
% Creates vision.mat. Generates training features for all of the training images.

	load('dictionary.mat');
	load('../data/traintest.mat');
    train_imagenames = train_imagenames{1,1};
   
	% TODO create train_features
    k = 100;
    histograms = cell (1,size(train_imagenames,1));
    for i = 1:size(train_imagenames,1)
        i
        pth = train_imagenames{i,1};
        pth1 = strrep (strrep (pth,'.jpg','.mat') , '.JPG', '.mat');
        pth1 = strcat(pth1);
        wfile = load(pth1);
        histograms{1,i} = getImageFeaturesSPM(3,wfile.wordMap,k); %this is 21 histograms
    end
    %%}
    train_features = cell2mat(histograms);
    whos train_features



	save('vision.mat', 'filterBank', 'dictionary', 'train_features', 'train_labels');

end