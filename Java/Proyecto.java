package scrum;

import java.util.Vector;

public class Proyecto {

    private String nombre;
    private String fechaInicio;
    private Boolean estado;
    public Vector<Equipo> equipos = new Vector<>();
    public Vector<Stakeholder> stakeholders = new Vector<>();
    public Vector<Tareas> tareas = new Vector<Tareas>();

    public Proyecto(String nombre, String fechaInicio, Boolean estado) {
        this.nombre = nombre;
        this.fechaInicio = fechaInicio;
        this.estado = estado;
    }
    
    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String aNombre) {
        this.nombre = aNombre;
    }

    public String getFechaInicio() {
        return this.fechaInicio;
    }

    public void setFechaInicio(String aFechaInicio) {
        this.fechaInicio = aFechaInicio;
    }

    public Boolean getEstado() {
        return this.estado;
    }

    public void setEstado(Boolean aEstado) {
        this.estado = aEstado;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Proyecto{");
        sb.append("nombre=").append(nombre);
        sb.append(", fechaInicio=").append(fechaInicio);
        sb.append(", estado=").append(estado);
        sb.append(", equipos=").append(equipos);
        sb.append(", stakeholders=").append(stakeholders);
        sb.append(", tareas=").append(tareas);
        sb.append('}');
        return sb.toString();
    }

}
