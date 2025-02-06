class Decision {

    private double COOLER_THREDHOLD = 28.0;
    private double HEATER_THREDHOLD = 20.0;
    HeaterAndCooler HEATER = HeaterAndCooler.HEATER;
    HeaterAndCooler COOLER = HeaterAndCooler.COOLER;
    HeaterAndCooler OFF = HeaterAndCooler.OFF;

    private Context cx;

    public Decision(Context cx) {
        this.cx = cx;
    }

    public HeaterAndCooler decideFunction() {
        double temperature = this.cx.getTemperature();
        if (temperature >= COOLER_THREDHOLD) {
            return COOLER;
        } else if (temperature <= HEATER_THREDHOLD) {
            return HEATER;
        } else {
            return OFF;
        }
    }
}