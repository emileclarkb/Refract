// Electron Module
const electron = require('electron');

const app = electron.app;
const BrowserWindow = electron.BrowserWindow;


var win;
// create window
function create()
{
    var appConfig =
    {
        width: 800,
		height: 600,
		x: 0,
		y: 0,
		darkTheme: true,
        fullscreen: true,
		webPreferences: {
			nodeIntegration: false,
		},
		backgroundColor: "#000000"
    };

    // Create the browser window.
    win = new BrowserWindow(appConfig);
    win.removeMenu(); // remove menu (File, Edit, etc.)

    

    // Flask
    //win.loadURL('http://localhost:5000');
    //const ses = win.webContents.session.clearCache();
}

app.on('ready', create);
