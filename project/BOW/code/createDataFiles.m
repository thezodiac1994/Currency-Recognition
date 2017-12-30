function [] = createDataFiles()
    f = '../../train_imagenames.csv';
    fid = fopen(f);
    train_imagenames = textscan(fid, '%s', 'Delimiter','\n'); % you will need to change the number of values to match your file %f for numbers and %s for strings.
    fclose (fid);
    save('../data/traintest.mat','train_imagenames');
    all_imagenames = train_imagenames;
    save('../data/traintest.mat','all_imagenames','-append');
    
    
    f = '../../train_labels.csv';
    fid = fopen(f);
    train_labels = textscan(fid, '%s', 'Delimiter','\n'); % you will need to change the number   of values to match your file %f for numbers and %s for strings.
    fclose (fid);
    save('../data/traintest.mat','train_labels','-append');
    
    f = '../../uniqueLabels.csv';
    fid = fopen(f);
    mapping = textscan(fid, '%s', 'Delimiter','\n'); % you will need to change the number   of values to match your file %f for numbers and %s for strings.
    mapping{1,1} = mapping{1,1}'; % make a row vector 
    fclose (fid);
    save('../data/traintest.mat','mapping','-append');
 
    
end