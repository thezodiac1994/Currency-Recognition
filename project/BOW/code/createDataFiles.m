function [] = createDataFiles()
    f = '../train_imagenames.csv';
    fid = fopen(f);
    train_imagenames = textscan(fid, '%s', 'Delimiter','\n'); % you will need to change the number   of values to match your file %f for numbers and %s for strings.
    fclose (fid);
    save('traintest.mat','train_imagenames');
    
    
    f = '../train_labels.csv';
    fid = fopen(f);
    train_labels = textscan(fid, '%s', 'Delimiter','\n'); % you will need to change the number   of values to match your file %f for numbers and %s for strings.
    fclose (fid);
    save('traintest.mat','train_labels','-append');
    
end