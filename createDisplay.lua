

local monitor = peripheral.find("monitor")
local width, height = term.getSize()
local msg = ""
local valid_options = {
    ResourcePlant = true,
    MainPlant = true,
    FoodProcessing = true,
    ComponentPlant = true,
    Anime = true
}
write("Create Mod Factory Display v1.0\n")
while not valid_options[msg] do
    write("Please Choose a Display Label (Options: MainPlant, ResourcePlant, ComponentPlant, FoodProcessing):\n")
    write("> ")
    msg = read()
    if valid_options[msg] then
        if msg == "ResourcePlant" then
            write("Label 'Resource Plant' Selected\n")
        elseif msg == "MainPlant" then
            write("Label 'Main Plant' Selected\n")
        elseif msg == "FoodProcessing" then
            write("Label 'Food Processing' Selected\n")
        elseif msg == "ComponentPlant" then
            write("Label 'Component Plant' Selected\n")
        elseif msg == "Anime" then
            write("Label 'Anime' Selected :)\n")
        break
        end
    else
        write("Invalid Display Label\n")
    end
end
textutils.slowWrite("Initializing Display...", 30)
term.clear()
if msg == "Anime" then

elseif msg == "ComponentPlant" then

elseif msg == "FoodProcessing" then

elseif msg == "MainPlant" then

elseif msg == "ResourcePlant" then

end


local stressometer = peripheral.find("stressometer ")
while true do
    local stress = stressometer.getStress()
    local capacity = stressometer.getStressCapacity()
    local percent = math.floor((stress/capacity)*100)
    
end