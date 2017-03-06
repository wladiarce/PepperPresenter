Attribute VB_Name = "Export"
Option Explicit

Sub Exporter(ByVal Control As IRibbonControl)
    Dim Presentation As Slides
    Dim Sl As Slide
    Dim Name As String
    Dim PresentationPath, SlidesPath As String
    
    Name = CreateObject("scripting.filesystemobject").GetBaseName(ActivePresentation.FullName)
    PresentationPath = ActivePresentation.Path & "\" & Name
    SlidesPath = ActivePresentation.Path & "\" & Name & "\slides"
    
    MkDir PresentationPath
    MkDir SlidesPath
    
    For Each Sl In ActivePresentation.Slides
        Sl.Export SlidesPath & "\slide" & Sl.SlideIndex & ".jpg", "JPG"
    Next Sl
    
    ActivePresentation.SaveAs PresentationPath & "\" & Name, ppSaveAsOpenXMLPresentation
    
    
    MsgBox "Correctly exported. Copy the folder " & Name & " created in the current path to Pepper"
End Sub
