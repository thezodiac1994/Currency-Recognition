function guessedImage = guessImage( imagename ) 
% Given a path to a scene image, guess what scene it is
% Input:
%   imagename - path to the image

	%fprintf('[Loading..]\n');
    load('vision.mat');
	load('../data/traintest.mat','mapping');
    mapping = mapping {1,1};
	image = im2double(imread(imagename));

%	imshow(image);
	%fprintf('[Getting Visual Words..]\n');
	wordMap = getVisualWords(image, filterBank, dictionary);
	h = getImageFeaturesSPM(3, wordMap, size(dictionary,2));
	distances = distanceToSet(h, train_features);
    
    knn = 3;
    knn_labels = cell(1,knn);
    train_labels = train_labels{1,1}
    for i = 1 : knn
        [~,nnI] = max(distances);
        nnI
        whos train_labels 
        whos knn_labels 
        knn_labels{1,i} = train_labels{nnI,1}
        distances(nnI) = -1;
    end
    
    
    % mean_closest = mode(knn_labels{:});
	% guessedImage = mapping{mean_closest};
	
    
    for i = 1:knn
        knn_labels{1,i} = str2num(['uint8(',knn_labels{1,i},')'])
    end
    labelmat = cell2mat(knn_labels);
    guessedImage = mode(labelmat(:));
    
    fprintf('[My Guess]:%s.\n',mapping{1,guessedImage});

	%figure(1);
	%imshow(image);
	%title('image to classify')

end
