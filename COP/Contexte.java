public class Contexte {
    private double temperature;

    public Context(){
        this.temperature = 0.0;
    }

    public Context(double temperature){
        this.temperature = temperature;
    }

    public void setTemperature(double temperature) {
        this.temperature = temperature;
    }

    public double getTemperature() {
        return this.temperature;
    }
}
