import package.LandingPanel 
import package.MainPanel

def showLanding(root):
    landing = package.LandingPanel.LandingPanel(root)
    landing.genLanding()

def showMain(root):
    main = package.MainPanel.MainPanel(root)
    main.genMainPanel()