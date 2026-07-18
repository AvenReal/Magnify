function initUi()
  local ref = app.registerUi({["menu"] = "Magnify", ["callback"] = "ExportCurrentPage", ["accelerator"] = "<Control>m"});
end

function ExportCurrentPage()
    local docStructure = app.getDocumentStructure()
    local filePath = docStructure["xoppFilename"] .. ".png"
    app.export({ ["outputFile"] = filePath , ["pngWidth"] = 800})
    -- os.execute("touch myyytest")
end
