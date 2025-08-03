# Azure Deployment Fix

## What I Fixed:

1. **Removed complex deployment scripts** that were causing failures on Linux
2. **Simplified startup configuration** for better compatibility
3. **Streamlined the deployment process**

## Required Azure Configuration:

### 1. Set Startup Command

Go to **Azure Portal** → Your **Web App** → **Settings** → **Configuration** → **General Settings**

Set the **Startup Command** to:
```
python startup.py
```

### 2. Ensure Python Version

In the same **General Settings** tab:
- **Stack**: Python
- **Major Version**: 3.12
- **Minor Version**: 3.12

### 3. Deploy Again

Now try deploying again using any of these methods:

#### Method A: Zip Deploy (Simplest)
1. Create a ZIP file of your entire project folder
2. Go to Azure Portal → Your Web App → **Development Tools** → **Advanced Tools (Kudu)**
3. Click **Go** → **Tools** → **Zip Push Deploy**
4. Drag and drop your ZIP file

#### Method B: Git Deploy
```bash
git add .
git commit -m "Fixed Azure deployment configuration"
git push azure main
```

#### Method C: Azure CLI
```bash
az webapp deployment source config-zip --resource-group your-resource-group --name your-web-app-name --src project.zip
```

## Verify Deployment:

1. **Check App Status**: Azure Portal → Web App → Overview (should show "Running")
2. **Test Health Endpoint**: `https://your-app-name.azurewebsites.net/health`
3. **Check Logs**: Azure Portal → Web App → Monitoring → Log stream

The deployment should now work successfully!