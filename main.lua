function initUi()
  local ref = app.registerUi({["menu"] = "Magnify", ["callback"] = "ExportCurrentPage", ["accelerator"] = "<Control>m"});
end

function ExportCurrentPage()
    local docStructure = app.getDocumentStructure()
    local filePath = docStructure["xoppFilename"]
    app.export({ ["outputFile"] = filePath, ["pngWidth"] = 800 })
    os.execute("/usr/bin/kitty /usr/bin/python3.12 /usr/share/xournalpp/plugins/Magnify/plugin.py " .. filePath )
    app.openDialog("Done", {"Ok"})
end
