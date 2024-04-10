def param_heatmap(method,fig,ax,xparam,yparam,mesh,xlabel,ylabel,bestx,besty,log=False):

    x, y = np.meshgrid(xparam,yparam)
    z = mesh#-np.log(np.abs(1-(mesh)+1e-8)) #scaling to emphasize upper range differences in AUC
    c = ax.pcolormesh(x, y, z, cmap='viridis', vmin=z.min(), vmax=z.max())
    ax.set_title(method)
    ax.axis([x.min(), x.max(), y.min(), y.max()])
    if log:
        ax.set_xscale('log')
    cbar =fig.colorbar(c,  ticks=[z.min(), np.median(z),z.max()],ax=ax)
    ax.scatter(bestx,besty,marker = "*",s = 10,color = 'r')
    #cbar.ax.set_yticklabels([round(1-np.exp(-z.min()),3), 0.5, round(1-np.exp(-z.max()),3)])
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)


def param_scatter(method,fig,ax,xparam,aucs,xlabel,log=False):
    x = xparam
    y = aucs
    c = ax.scatter(x,y)
    ax.set_title(method)
    ax.axis([x.min(), x.max(), y.min(), y.max()])
    ax.set_xlabel(xlabel)
    ax.set_ylabel('AUC')
    if log:
        ax.set_xscale('log')

def decision_boundary_plot(x_train, x_test, y_test, models,Method):
  colors = ['g','r','b','m']
  #fig, axs = plt.subplots(2,2,figsize=(10,10))
  fig, axs = plt.subplots(1,1)
  an_idx = np.where(y_test == 1)
  bg_idx = np.where(y_test == 0)

  xsteps = 50
  ysteps = 50
  xmin = np.min(x_train[:,0])*1.1
  ymin = np.min(x_train[:,1])*1.1
  xmax = np.max(x_train[:,0])*1.1
  ymax = np.max(x_train[:,1])*1.1


  xx,yy = np.meshgrid(np.linspace(xmin,xmax,xsteps), np.linspace(ymin,ymax,ysteps))
  grid_dims = xx.shape
  xx_f = np.expand_dims(xx.flatten(),axis=1)
  yy_f = np.expand_dims(yy.flatten(),axis=1)
  grid_list = np.concatenate((xx_f,yy_f),axis = 1)


  axs_ = np.reshape(axs,len(models))
  for i in range(len(models)):
    axs_[i].scatter(x_train[:,0], x_train[:,1],s=10,label = None, color = 'k',marker='s', edgecolors='k',alpha = 0.8)
    axs_[i].scatter(x_test[bg_idx,0], x_test[bg_idx,1],s=10,label = None, color = 'b',marker='s', edgecolors='b',alpha = 0.5)
    axs_[i].scatter(x_test[an_idx,0],x_test[an_idx,1], s=10,label = None, color = 'r',marker='s', edgecolors='r',alpha = 0.5)

    grid_errs = np.reshape(np.expand_dims(models[i].decision_function(grid_list),axis=1),grid_dims)

    bgval_idx = np.where(y_val == 0)
    scores = models[i].decision_function(x_val)
    fixed = np.max(scores[bgval_idx])
    cntr1 = axs_[i].contour(xx,yy,grid_errs,[fixed],colors=colors[i])
    #axs_[i].axis('off')
    axs_[i].set_xlim(xmin,xmax)
    axs_[i].set_ylim(ymin,ymax)
    axs_[i].set_title(Method)
    plt.subplots_adjust(wspace=0.25, hspace=0.25)



def ROC_curve(y_test, scores, key):
  methods = ['kPCA','PCA','ParzenWindow','OCSVM']
  fig, ax = plt.subplots(figsize=(7,7))
  colors = ['g','r','b','m']
  for i in range(len(methods)):
      fpr,tpr,_ = metrics.roc_curve(y_test,scores[i],drop_intermediate = False)
      tpr[1] = 0
      if test_aucs[i] == 0.5:
          fpr = np.linspace(0,1,100)
          tpr = fpr
      ax.plot(fpr,tpr, color = colors[i], marker='o',label = methods[i],ms=2)
  x=np.linspace(0,1,100)
  y = x
  ax.plot(x,y,ls = "--",label='random')
  ax.set_xlim([1e-4,1])
  ax.legend()
  ax.set_title(key+' ROC')
  ax.set_xlabel('False Positive Rate')
  ax.set_ylabel('True Positive Rate')
  ax.set_xscale('log')


def check_d(edge,point,thresh):
    n = edge.shape[0]
    p_exp = np.repeat(np.expand_dims(point,axis=0),n,axis=0)
    diff = edge - p_exp
    dist = np.sqrt(diff[:,0]*diff[:,0] + diff[:,1]*diff[:,1])
    if np.min(dist) > thresh:
        return True
    else:
        return False

