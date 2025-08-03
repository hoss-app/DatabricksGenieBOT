# Azure Deployment Guide for Databricks Genie Bot

## Fixed Issues

The following issues have been resolved for Azure deployment:

1. **Environment Variable Validation**: Added proper validation for required environment variables
2. **Logging Configuration**: Improved logging for Azure environment with proper format
3. **Health Check Endpoints**: Added `/` and `/health` endpoints for Azure health monitoring
4. **Port Configuration**: Fixed port binding to use Azure's `PORT` environment variable
5. **Startup Scripts**: Created proper startup configuration for Azure Web Apps
6. **Web.config**: Updated for modern Azure Python deployment
7. **Deployment Scripts**: Added Azure-specific deployment configuration

## Deployment Steps

### 1. Azure Resources Setup

Create these resources in Azure Portal:

- **App Service Plan** (Linux, Python 3.12)
- **Web App** (Python 3.12 runtime)
- **Azure Bot Service** (for Teams integration)

### 2. Environment Variables Configuration

In your Azure Web App → Settings → Configuration → Application Settings, add:

```
DATABRICKS_SPACE_ID=your_space_id_here
DATABRICKS_HOST=https://adb-xxxxxxxxx.xx.azuredatabricks.net
DATABRICKS_TOKEN=your_databricks_token_here
MicrosoftAppId=your_bot_app_id_here
MicrosoftAppPassword=your_bot_app_password_here
```

### 3. Bot Service Configuration

1. Go to your Azure Bot Service
2. Set the **Messaging Endpoint** to: `https://your-web-app-name.azurewebsites.net/api/messages`
3. Configure the **Microsoft App ID** and **Password** from your bot registration
4. Enable the **Microsoft Teams** channel

### 4. Deployment Options

#### Option A: Azure CLI Deployment
```bash
# Login to Azure
az login

# Deploy the web app
az webapp up --name your-web-app-name --resource-group your-resource-group --runtime "PYTHON:3.12"
```

#### Option B: GitHub Actions (Recommended)
1. Fork/clone this repository
2. Go to your Web App → Deployment Center
3. Connect to your GitHub repository
4. Azure will automatically create GitHub Actions workflow

#### Option C: Local Git Deployment
```bash
# Add Azure remote
git remote add azure https://your-web-app-name.scm.azurewebsites.net:443/your-web-app-name.git

# Deploy
git push azure main
```

### 5. Verify Deployment

1. **Health Check**: Visit `https://your-web-app-name.azurewebsites.net/health`
   - Should return: `{"status": "healthy", "service": "Databricks Genie Bot"}`

2. **Bot Test**: Use the "Test in Web Chat" feature in Azure Bot Service

3. **Teams Test**: Add the bot to Microsoft Teams and send a test message

### 6. Troubleshooting

#### Check Application Logs
```bash
# Using Azure CLI
az webapp log tail --name your-web-app-name --resource-group your-resource-group

# Or via Azure Portal: Web App → Monitoring → Log stream
```

#### Common Issues and Solutions

1. **"Service Unavailable" Error**
   - Check if all environment variables are set
   - Verify the startup command in Configuration → General Settings

2. **Bot Not Responding**
   - Verify the messaging endpoint URL
   - Check that MicrosoftAppId and MicrosoftAppPassword are correct
   - Ensure the bot is published and channels are configured

3. **Databricks Connection Issues**
   - Verify DATABRICKS_HOST URL format (must include https://)
   - Check that DATABRICKS_TOKEN has proper permissions
   - Validate DATABRICKS_SPACE_ID exists and is accessible

4. **Timeout Issues**
   - Default timeout is 4 minutes (configured in web.config)
   - For long-running queries, consider implementing async patterns

### 7. Performance Optimization

1. **Enable Application Insights** for monitoring and diagnostics
2. **Scale up** the App Service Plan if needed for production workloads
3. **Configure auto-scaling** based on CPU/memory usage
4. **Enable Application Logging** for troubleshooting

### 8. Security Considerations

1. **Never commit** `.env` files with secrets
2. **Use Azure Key Vault** for sensitive configuration in production
3. **Enable HTTPS Only** in Web App settings
4. **Configure proper CORS** if accessing from web clients
5. **Regular security updates** for Python packages

## Files Modified/Created

- `app.py` - Enhanced with Azure-specific configurations
- `startup.py` - Azure startup script
- `web.config` - Azure deployment configuration
- `gunicorn.conf.py` - Production server configuration
- `deploy.cmd` - Azure deployment script
- `.deployment` - Kudu deployment configuration
- `runtime.txt` - Python runtime specification

## Support

For issues:
1. Check Azure Web App logs
2. Verify all environment variables are set
3. Test health endpoint first
4. Validate bot credentials in Azure Portal