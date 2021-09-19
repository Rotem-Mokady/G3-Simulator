class TDHbyFlow:
    ID = "tdh-by-flow"

    class Pipe:
        AUTO_COMPLETE = "missing value in Pipe Height"
        MODE = "numeric"
        DEFAULT = 5
        MIN = 0
        NAME = "Pipe Height (meters)"
        TYPE = "number"

    class Diameter:
        AUTO_COMPLETE = "missing value in Diameter Height"
        MODE = "numeric"
        DEFAULT = 10
        MIN = 0
        NAME = "Pipe Diameter (millimeters)"
        TYPE = "number"

    class PipeType:
        AUTO_COMPLETE = "missing value in Pipe Type"
        NAME = 'Pipe Type ("PVC, HOPE", "NEW GI" or "OLD GI")'
        SEARCHABLE = False
