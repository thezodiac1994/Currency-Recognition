function [] = createTestData()
    f = '../../test_imagenames.csv';
    fid = fopen(f);
    test_imagenames = textscan(fid, '%s', 'Delimiter','\n'); % you will need to change the number of values to match your file %f for numbers and %s for strings.
    fclose (fid);
    save('../data/traintest.mat','test_imagenames');
    f = '../../test_labels.csv';
    fid = fopen(f);
    test_labels = textscan(fid, '%s', 'Delimiter','\n'); % you will need to change the number   of values to match your file %f for numbers and %s for strings.
    fclose (fid);
    save('../data/traintest.mat','test_labels','-append');
    
    f = '../../uniqueLabels.csv';
    fid = fopen(f);
    mapping = textscan(fid, '%s', 'Delimiter','\n'); % you will need to change the number   of values to match your file %f for numbers and %s for strings.
    mapping{1,1} = mapping{1,1}'; % make a row vector 
    fclose (fid);
    save('../data/traintest.mat','mapping','-append');
end