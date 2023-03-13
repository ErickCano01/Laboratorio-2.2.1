package scrum;

public class Stakeholder {

    private float presupuesto;
    private String nombre;
    private int id;

    public Stakeholder(float presupuesto, String nombre, int id) {
        this.presupuesto = presupuesto;
        this.nombre = nombre;
        this.id = id;
    }
    
    

    public float getPresupuesto() {
        return this.presupuesto;
    }

    public void setPresupuesto(float aPresupuesto) {
        this.presupuesto = aPresupuesto;
    }

    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String aNombre) {
        this.nombre = aNombre;
    }

    public int getId() {
        return this.id;
    }

    public void setId(int aId) {
        this.id = aId;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Stakeholder{");
        sb.append("presupuesto=").append(presupuesto);
        sb.append(", nombre=").append(nombre);
        sb.append(", id=").append(id);
        sb.append('}');
        return sb.toString();
    }

}
