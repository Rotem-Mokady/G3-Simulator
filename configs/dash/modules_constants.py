class TDHbyFlow:
    ID = "tdh-by-flow-inputs"

    class PipeHeight:
        ID = "tdh-by-flow-pipe"
        AUTO_COMPLETE = "missing value in Pipe Height"
        MODE = "numeric"
        DEFAULT = 5
        MIN = 0
        NAME = "Pipe Height (meters)"
        TYPE = "number"

    class PipeDiameter:
        ID = "tdh-by-flow-diameter"
        AUTO_COMPLETE = "missing value in Diameter Height"
        MODE = "numeric"
        DEFAULT = 10
        MIN = 0
        NAME = "Pipe Diameter (millimeters)"
        TYPE = "number"

    class PipeType:
        ID = "tdh-by-flow-pipe-type"
        AUTO_COMPLETE = "missing value in Pipe Type"
        NAME = 'Pipe Type'
        SEARCHABLE = False

    class Graph:
        ID = "tdh-by-flow-graph"
