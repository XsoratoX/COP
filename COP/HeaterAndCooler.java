public enum HeaterAndCooler {

    OFF("Off", 0),
    HEATER("Heater", 1),
    COOLER("Cooler", 2);

    private String label;
    private int id;

    private HeaterAndCooler(String label, int id) {
        this.label = label;
        this.id = id;
    }

    public String getLabel() {
        return label;
    }

    public int getId() {
        return id;
    }
}