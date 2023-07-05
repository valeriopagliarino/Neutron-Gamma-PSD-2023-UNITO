with open('model/trained.p', 'rb') as handle:
    finalmetrics = pickle.load(handle)
finalhistory = finalmetrics['history']
    
#kfoldhistories = []
fold_nos = [1,3,5,7,9,11]

with open('./model/trained_model_metrics.p', 'rb') as handle:
    kfoldmetrics = pickle.load(handle)
kfoldhistories = kfoldmetrics['histories']

#kfoldhistories = []
fold_nos = [2,4,6,8,10,12]

with open('./model/trained_model_metrics.p', 'rb') as handle:
    kfoldmetrics = pickle.load(handle)
kfoldhistories = kfoldmetrics['histories']

sb.set_theme(style='darkgrid')

# path to final model histories: /media/workStorage1/vpagliarino/OsellaNN-2023-UNITO/model/trained
sns.color_palette("tab10")
f, axes = plt.subplots(nrows=1, ncols=2,figsize=(10, 5))
#f.suptitle('Transfer Learning', fontsize=18)
#sb.despine(f)

bins= list(np.arange(1,8,1))
#sb.despine(f)

# VALIDATION LOSS FINAL MODEL
df = pd.DataFrame()
df['x']= bins
df['Validation']=finalhistory.history['val_loss'][0:7]

dfm = df.melt('x', var_name='Loss', value_name='vals')
print(df)
sb.lineplot(
    data=dfm,
    x='x',
    y='vals',
    hue='Loss',
    ax=axes[0],
    color=sns.color_palette()[fold_no],
    ci=None
)

# TRAINING LOSSES FOR FOLDS 2,4,6,8,10,12
for fold_no in range(len(fold_nos)): 
    df = pd.DataFrame()
    df['x']= bins
    df['Training']=kfoldhistories[fold_no*2].history['loss']
    
    dfm = df.melt('x', var_name='Loss', value_name='trains')
    print(df)
    sb.lineplot(
        data=dfm,
        x='x',
        y='trains',
        hue='Loss',
        color=sns.color_palette()[fold_no],
        ax=axes[0],
        ci=None
    )
axes[0].set(xlabel ="Epoch", ylabel = "Loss", title = "Loss vs Epoch")
#plt.legend(labels = ['Final model', 'Fold 2', 'Fold 4', 'Fold 6', 'Fold 8', 'Fold 10', 'Fold 12'])

model.load_weights('./model/fullTraining.h5')
y_predicted = model.predict(testSetValues.transpose()[0:240].transpose())
fpr, tpr, thresholds = roc_curve(testSetLabels, y_predicted, pos_label=1)
    
# MODEL ROC ON TEST SET
df = pd.DataFrame()
df['Testfpr']= fpr
df['Testtpr']= tpr

sb.lineplot(
    data=df,
    x='Testfpr',
    y='Testtpr',
    ax=axes[1],
    color='blue',
    linewidth = 1.,
    ci=None
)

# VALIDATION SET ROC AUCS FOR FOLDS 2,4,6,8,10,12
weightnames = ['kfold_2.h5','kfold_4.h5','kfold_6.h5','kfold_8.h5','kfold_10.h5','kfold_12.h5']
for train, test in kfold.split(X_train, y_train):
    fold_no = 0
    model.load_weights('./model/' + weightnames[fold_no/2])
    y_predicted = model.predict(X_train[test].transpose()[0:240].transpose())
    fpr, tpr, thresholds = roc_curve(y_train[test], y_predicted, pos_label=1)
    df = pd.DataFrame()
    df['Valfpr']= fpr
    df['Valtpr']= tpr
    
    sb.lineplot(
        data=df,
        x='Valfpr',
        y='Valtpr',
        ax=axes[1],
        color=sns.color_palette()[fold_no/2],
        linewidth = 1.,
        ci=None
    )
    
    fold_no += 2

axes[1].set(xlabel ="False Positive Rate", ylabel = "True Positive Rate", title = "ROC Curve",ylim=(0.9, 1.02),xlim=(-0.015, .1))
plt.legend(labels = ['Final model', 'Fold 2', 'Fold 4', 'Fold 6', 'Fold 8', 'Fold 10', 'Fold 12'])

f.savefig("./Fig3.pdf")
